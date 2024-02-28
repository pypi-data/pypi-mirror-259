from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import pyttsx3

if TYPE_CHECKING:
  from typing import Any

  from terminal.core import PrinterSettings, Terminal

engine: pyttsx3.engine.Engine = pyttsx3.init()

# Just in case anything else wants to tap into this for some reason.
async def play_message(message: str) -> None:
  def _inner(message: str):
    if engine.isBusy():
      engine.stop()
    engine.say(message)
    engine.runAndWait()

  loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
  await loop.run_in_executor(None, _inner, message)

async def _audio_callback(terminal: Terminal, print_settings: PrinterSettings, raw_message: str, args: list[str], kwargs: dict[str,Any], formatted_message: str, output_message: str) -> None:
  # We only really care about the formatted message,
  # as the announcer doesn't need to speak the time.

  # Clean up the numbers for the TTS announcer.
  msg = formatted_message

  success = False
  while not success:
    try:
      await play_message(msg)
      success = True
    except RuntimeError:
      await asyncio.sleep(0.5)

def install(terminal: Terminal) -> None:
  "Install the audio output on the terminal object."
  terminal.add_print_callback(_audio_callback, background=True)