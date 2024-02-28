from __future__ import annotations

from typing import TYPE_CHECKING

from .exceptions import CommandAlreadyExists, CommandNotFoundException

if TYPE_CHECKING:
  from typing import Any, Awaitable, Callable

  from .core import Terminal
  from .exceptions import TerminalException

async def command_not_found_handler(term: Terminal, exception: CommandNotFoundException):
  await term.print("Command {0} not found!", str(exception))

async def command_already_exists_handler(term: Terminal, exception: CommandAlreadyExists):
  await term.print("Command {0} already registered!", str(exception))

specific_handlers: dict[TerminalException, list[Callable[[Any, Any], Awaitable[Any]]]] = {
  CommandNotFoundException: [
    command_not_found_handler
  ],
  CommandAlreadyExists: [
    command_already_exists_handler
  ]
}