from __future__ import annotations

import typing
import shlex
import inspect

if typing.TYPE_CHECKING:
  from typing import Callable, Awaitable, Any

# Take a function, and a list of arguments, and return casted arguments
# to pass to the function.

def evaluate_annotation(anno: Any, globals: dict[str, Any], locals: dict[str, Any], cache: dict[str, Any], *, implicit_str: bool = True) -> Any:
  if isinstance(anno, str):
    implicit_str = True
  
  if implicit_str and isinstance(anno, str):
    if anno in cache:
      return cache[anno]
    evaluated = eval(anno, globals, locals)
    cache[anno] = evaluated
    return evaluated
  

def transform(func: Callable[[Any, Any], Awaitable[Any]], *args, required_parameters: int = 0) -> dict[str, Any]:
  "Take in a function, and arguments from shlex, and returns kwargs."
  signature = inspect.signature(func)
  # Just pass one at a time
  arglist = list(args)
  anno_cache: dict[str, Any] ={}
  kwargs = {}

  if len(signature.parameters) < required_parameters:
    raise TypeError(f"Command signature requires at least {required_parameters - 1} parameter(s)")

  for name, para in signature.parameters.items():
    if required_parameters != 0: # Stupid simple way to skip self and ctx
      required_parameters -= 1
      continue

    match para.kind:
      case inspect.Parameter.POSITIONAL_OR_KEYWORD:
        raw_arg = arglist.pop(0)
        # This is a normal parameter. Try to interpret it.
        if not isinstance(para.annotation, inspect._empty):
          try:
            converter = evaluate_annotation(para.annotation, globals(), globals(), anno_cache)
            arg = converter(raw_arg)
          except ValueError:
            arg = raw_arg
          kwargs[name] = arg
        else:
          kwargs[name] = raw_arg
      case inspect.Parameter.VAR_POSITIONAL:
        # This is a *args, so give the rest of the arglist to it.
        # This should also be the end of the parameters.
        kwargs[name] = arglist
        break
      case inspect.Parameter.KEYWORD_ONLY:
        # This is after the args, so give the arglist as a joined string to it.
        kwargs[name] = shlex.join(arglist)
        break
  # Now we have all the kwargs.
  return kwargs
