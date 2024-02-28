from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from typing import Callable, Any

def is_inside_class(func: Callable[..., Any]) -> bool:
  if func.__qualname__ == func.__name__:
    return False
  (remaining, _, _) = func.__qualname__.rpartition(">")
  return not remaining.endswith("<locals>")