from __future__ import annotations

import asyncio
import datetime
import logging
import shlex
from typing import TYPE_CHECKING  # , get_type_hints
from zoneinfo import ZoneInfo

from aioconsole import ainput, aprint

from .default_handlers import specific_handlers as default_error_handlers
from .exceptions import (CogAlreadyLoaded, CommandAlreadyExists,
                         CommandException, CommandNotFoundException,
                         TerminalException)
from .utils.load_extension import get_extension
from .utils.transformer import transform
from .utils.utils import is_inside_class

if TYPE_CHECKING:
  from typing import Any, Awaitable, Callable

LOG = logging.getLogger(__name__)

class PrinterSettings:
  include_date: bool = False
  include_time: bool = True
  command_prefix: str = "$ "
  output_prefix: str = ""
  date_format: str = "[%Y/%m/%d]"
  time_format: str = "[%H:%M:%S]"
  timezone: ZoneInfo = ZoneInfo("America/Toronto")

class Callback:
  callback: Callable[[Any, Any], Awaitable[Any]]
  background: bool # Determine whether or not the terminal must wait for the callback to finish before continuing.
  cog: Cog = None # If the callback is inside a cog or not.

  def __init__(self, callback: Callable[[Any, Any], Awaitable[Any]], background: bool = False, cog: Cog = None) -> None:
    self.callback = callback
    self.background = background
    self.cog = cog

class Terminal:
  _commands: set[Command] # Just a list of commands.
  _command_lookup: dict[str, Command] # Easy command lookup
  _cogs: set[Cog]
  _cog_lookup: dict[str, Cog]
  # Print callbacks take the following arguments:
  # print_settings: PrinterSettings | The printer settings object in user.
  # raw_message: str
  # args: list[str]
  # kwargs: dict[str]
  # formatted_message: str | The formatted message based off of the raw message, args, and kwargs.
  # output_message: str | The message to be printed to the console.
  _print_callbacks: set[Callback]
  _print_settings: PrinterSettings
  _message_callbacks: set[Callback]
  running: bool
  _global_error_handlers: set[Callback]
  _error_handlers: dict[TerminalException, Callback]
  awaiting_input: bool # Whether or not the terminal is awaiting user input.

  def __init__(self, print_settings: PrinterSettings = None, *, use_default_handlers: bool = True, custom_error_handlers: dict[TerminalException, list[Callable[[Any, Any], Awaitable[Any]]]] = None) -> None:
    if print_settings is None:
      print_settings = PrinterSettings()
    self._print_settings = print_settings
    self.running = True
    self._commands = set()
    self._command_lookup = {}
    self._cogs = set()
    self._cog_lookup = {}
    self._print_callbacks = set()
    self._message_callbacks = set()
    self._global_error_handlers = set()
    self._error_handlers = {}
    if use_default_handlers:
      self.add_error_handlers(default_error_handlers)
    elif custom_error_handlers is not None:
      self.add_error_handlers(custom_error_handlers)
    # If both of these are false/empty, the terminal will just have no default handlers.

  def add_error_handlers(self, handlers: dict[TerminalException, list[Callable[[Any, Any], Awaitable[Any]]]]):
    for exception_type, error_handlers in handlers.items():
      for handler in error_handlers:
        self.add_error_handler(exception_type, handler)

  def add_command(self, command: Command) -> bool:
    if command.name in self._command_lookup:
      raise CommandAlreadyExists(command.name)
    self._commands.add(command)
    self._command_lookup[command.name] = command
    return True

  def add_cog(self, cog: Cog) -> bool:
    if cog in self._cogs:
      raise CogAlreadyLoaded(cog.__class__.__qualname__)
    self._cogs.add(cog)
    self._cog_lookup[cog.__class__.__qualname__] = cog

    for command in cog._commands:
      self.add_command(command)
    for error_handler in cog._error_handlers:
      self.add_error_handler(error_handler.exception_type, error_handler._callback, background=error_handler.background, cog=error_handler._cog)
    
    return True

  def _remove_callback(self, callbacks: set[Callback], callback: Callable|Callback) -> None:
    if isinstance(callback, Callback):
      callback = callback.callback
    for cb in callbacks:
      if cb.callback == callback:
        callbacks.remove(cb)
        return

  def add_print_callback(self, callback: Callable[[Any, Any], Awaitable[Any]], *, background: bool = False) -> None:
    cb = Callback(callback, background)
    self._print_callbacks.add(cb)

  def remove_print_callback(self, callback: Callable[[Any, Any], Awaitable[Any]]) -> None:
    self._remove_callback(self._print_callbacks, callback)

  def add_message_callback(self, callback: Callable[[Any, Any], Awaitable[Any]], *, background: bool = False) -> None:
    cb = Callback(callback, background)
    self._message_callbacks.add(cb)

  def remove_message_callback(self, callback: Callable[[Any, Any], Awaitable[Any]]) -> None:
    self._remove_callback(self._message_callbacks,callback)

  def add_global_error_handler(self, callback: Callable[[Terminal, TerminalException], Awaitable[None]], *, background: bool = False) -> None:
    cb = Callback(callback, background)
    self._global_error_handlers.add(cb)

  def remove_global_error_handler(self, callback: Callable[[Terminal, TerminalException], Awaitable[None]]) -> None:
    self._remove_callback(self._global_error_handlers,callback)

  def add_error_handler(self, exception_type: TerminalException, callback: Callable[[Terminal, TerminalException], Awaitable[None]], *, background: bool = False, cog: Cog = None) -> None:
    if exception_type not in self._error_handlers:
      self._error_handlers[exception_type] = set()
    cb = Callback(callback, background, cog)
    self._error_handlers[exception_type].add(cb)

  def remove_error_handler(self, exception_type: TerminalException, callback: Callable[[Terminal, TerminalException], Awaitable[None]]) -> None:
    if exception_type not in self._error_handlers:
      return
    self._remove_callback(self._error_handlers[exception_type],callback)

  def _call_callback(self, callback: Callback, *args, **kwargs) -> asyncio.Task:
    fn = callback.callback
    if is_inside_class(fn):
      return asyncio.create_task(fn(callback.cog, *args, **kwargs))
    else:
      return asyncio.create_task(fn(*args, **kwargs))

  async def _call_callbacks(self, callback_list: set[Callback], *args, **kwargs) -> None:
    try:
      background_tasks = [self._call_callback(callback, *args, **kwargs) for callback in callback_list if callback.background]  # noqa: F841
      foreground_tasks = [self._call_callback(callback, *args, **kwargs) for callback in callback_list if not callback.background]
      await asyncio.gather(*foreground_tasks) # Theoretically, the background tasks run regardless.
    except Exception as e:
      await self.throw_exception(e)

  async def print(self, message: str, *args, **kwargs) -> None:
    "Use of skip_callbacks is important if the callback is a message_callback. Else, infinite loop."
    return await self._print(message, *args, **kwargs)

  async def _print(self, message: str, *args, skip_callbacks: bool = False, **kwargs) -> None:
    "Method to print to the console, prefixed by some settings"

    formatted_message = message.format(*args, **kwargs)

    current_date = datetime.datetime.now(self._print_settings.timezone)

    msg_date = current_date.strftime(self._print_settings.date_format) if self._print_settings.include_date else ""
    msg_time = current_date.strftime(self._print_settings.time_format) if self._print_settings.include_time else ""

    output_message = "{0}{1} {2}{3}".format(msg_date,msg_time,self._print_settings.output_prefix,formatted_message)

    if not skip_callbacks:
      await self._call_callbacks(self._print_callbacks, self, self._print_settings, message, list(args), dict(kwargs), formatted_message, output_message)
    
    # Now just print the output
    if self.awaiting_input:
      await aprint()
      await aprint(output_message)
      await aprint(self._print_settings.command_prefix, end="")
    else:
      await aprint(output_message)

  async def create_context(self, message: str) -> Context:
    # Find what command to execute.
    if not message:
      return None
    escaped = message.replace("'", "\\'")
    split = shlex.split(escaped)
    command_name = split[0]
    valid = True
    if command_name not in self._command_lookup:
      valid = False
    command = self._command_lookup.get(command_name, None)

    ctx = Context(self, command, command_name, split[1:], valid)
    return ctx

  async def invoke_command(self, ctx: Context) -> None:
    command = ctx.command
    args = ctx._args

    try:
      if is_inside_class(command._callback):
        kwargs = transform(command._callback, *args, required_parameters=2)
        await command._callback(command._cog, ctx, **kwargs)
      else:
        kwargs = transform(command._callback, *args, required_parameters=1)
        await command._callback(ctx, **kwargs)
    except Exception as e:
      await self.throw_exception(CommandException, command, ctx, e)

  async def throw_exception(self, exception: TerminalException, *args, **kwargs):
    # Throw a global exception.
    await self._call_callbacks(self._global_error_handlers, self, exception, *args, **kwargs)

  async def run(self):
    "Launch the async terminal, receiving user input and running it through commands."
    # Basically a while loop of reading input, processing it.
    self.running = True
    while self.running:
      try:
        self.awaiting_input = True
        message = await ainput(self._print_settings.command_prefix)
        self.awaiting_input = False
      except EOFError:
        await aprint()
        await self._print("^D was pressed. Exiting.")
        self.running = False
      except KeyboardInterrupt:
        await aprint()
        await self._print("^C was pressed. Exiting.")
        self.running = False

      if not self.running:
        return

      # Run it through the message callbacks.
      await self._call_callbacks(self._message_callbacks, self, message)

      ctx = await self.create_context(message)
      if ctx.valid:
        # There was a valid context, invoke it.
        await self.invoke_command(ctx)
      else:
        exception = CommandNotFoundException(ctx.invoked_with)
        await self.throw_exception(exception)
        if CommandNotFoundException in self._error_handlers:
          await self._call_callbacks(self._error_handlers[CommandNotFoundException], self, exception)

  def stop(self):
    "Stop the loop."
    self.running = False

  async def load_extension(self, extension_name: str) -> None:
    "Load an extension, and call it's setup() function."
    module = get_extension(extension_name)
    if getattr(module, "setup"):
      await module.setup(self)

class Command:
  _callback: Callable[[Any, Any], Awaitable[Any]]
  name: str
  _cog: Cog = None

  def __init__(
    self,
    *,
    callback: Callable[[Any, Any], Awaitable[Any]],
    name: str
  ) -> None:
    self._callback = callback
    self.name = name

  @classmethod
  def create(cls, *, name: str = None):
    def decorator(func: Callable):
      result = cls(callback=func, name=name or func.__name__)
      return result
    return decorator

class ErrorHandler:
  _callback: Callable[[Any, Any], Awaitable[Any]]
  exception_type: TerminalException
  background: bool
  _cog: Cog = None
  def __init__(
    self,
    *,
    callback: Callable[[Any, Any], Awaitable[Any]],
    exception_type: TerminalException,
    background: bool = False
  ) -> None:
    self._callback = callback
    self.exception_type = exception_type
    self.background = background

  @classmethod
  def create(cls, *, exception_type: TerminalException, background: bool = False):
    def decorator(func: Callable):
      result = cls(callback=func, exception_type=exception_type, background=background)
      return result
    return decorator

class Cog:
  _commands: set[Command]
  _error_handlers: set[ErrorHandler]
  _terminal: Terminal = None

  def __init__(self) -> None:
    self._commands = set()
    self._error_handlers = set()

    command_objects = [getattr(self, attr_name) for attr_name in dir(self) if isinstance(getattr(self, attr_name), Command)]

    for command_object in command_objects:
      command_object._cog = self
      self.add_command(command_object)

    error_handler_objects = [getattr(self, attr_name) for attr_name in dir(self) if isinstance(getattr(self, attr_name), ErrorHandler)]

    for error_handler_object in error_handler_objects:
      error_handler_object._cog = self
      self.add_error_handler(error_handler_object)

  def add_command(self, command: Command) -> bool:
    if self._terminal is not None:
      self._terminal.add_command(command)
    self._commands.add(command)
    return command in self._commands

  def add_error_handler(self, handler: ErrorHandler) -> bool:
    if self._terminal is not None:
      self._terminal.add_error_handler(handler.exception_type, handler._callback, background=handler.background)
    self._error_handlers.add(handler)
    return handler in self._error_handlers

class Context:
  terminal: Terminal
  command: Command
  invoked_with: str
  args: list[str]
  valid: bool

  def __init__(self, 
    terminal: Terminal,
    command: Command,
    invoked_with: str,
    arguments: list[str],
    valid: bool = True
  ) -> None:
    self.terminal = terminal
    self.command = command
    self.invoked_with = invoked_with
    self._args = arguments
    self.valid = valid

  async def send(self, msg: str, *args, **kwargs) -> None:
    await self.terminal._print(msg, *args, **kwargs)