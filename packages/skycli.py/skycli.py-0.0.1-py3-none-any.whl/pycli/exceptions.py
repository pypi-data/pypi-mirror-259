from __future__ import annotations

class TerminalException(Exception):
  "The base class from which all extensions are subclassed."

# Command Errors

class CommandException(TerminalException):
  "The class from which all command related exceptions are subclassed."

class CommandNotFoundException(CommandException):
  "Raised when a command is not found, and passed to error handlers."

class CommandAlreadyExists(CommandException):
  "Raised when trying to register a command under the same name as another."
  def __init__(self, command_name: str) -> None:
    super().__init__(f"{command_name} is already loaded!")

# User input errors

class UserInputException(CommandException):
  "Base class for user input errors"

class MissingRequiredArgument(UserInputException):
  def __init__(self, argument_name: str) -> None:
    super().__init__(f"Missing {argument_name} which is a required argument!")

# Cog Errors

class CogException(TerminalException):
  "The class from which all cog related exceptions are subclassed."

class CogAlreadyLoaded(CogException):
  "Raised when a cog is already added to the terminal."
  def __init__(self, cog_name: str) -> None:
    super().__init__(f"{cog_name} is already loaded!")