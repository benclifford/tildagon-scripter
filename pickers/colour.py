import math

from tildagonos import tildagonos
from system.eventbus import eventbus
from events.input import BUTTON_TYPES, ButtonDownEvent

NICE_COLOURS = [(255,0,0), (0,255,0), (0,0,255), (255,255,255), (0,0,0),
                (255,255,0), (255,0,255), (0,255,255)]

class ColourPicker:

  def __init__(self, app, callback):
    self.app = app
    self.chosen_colour = 0
    self.rgb = NICE_COLOURS[self.chosen_colour]
    self._callback = callback
    eventbus.on(ButtonDownEvent, self._handle_buttondown, self.app)

  def update(self, delta):
    assert self.chosen_colour >= 0
    assert self.chosen_colour < len(NICE_COLOURS)
    self.rgb = NICE_COLOURS[self.chosen_colour]
    for n in range(0,12):
      tildagonos.leds[n+1] = self.rgb
    tildagonos.leds.write()

  def draw(self, ctx):

    ctx.arc(0, 0, 60, 0, 2 * math.pi, True)
    ctx.rgb(*self.rgb).fill()

  def _cleanup(self):
    eventbus.remove(ButtonDownEvent, self._handle_buttondown, self.app)

  def _handle_buttondown(self, event):
    if BUTTON_TYPES["UP"] in event.button:
      self.chosen_colour = (self.chosen_colour + 1) % len(NICE_COLOURS)
      assert self.chosen_colour >= 0
      assert self.chosen_colour < len(NICE_COLOURS)
    elif BUTTON_TYPES["DOWN"] in event.button:
      self.chosen_colour = (self.chosen_colour + 1) % len(NICE_COLOURS)
      assert self.chosen_colour >= 0
      assert self.chosen_colour < len(NICE_COLOURS)
    elif BUTTON_TYPES["CONFIRM"] in event.button:
      eventbus.remove(ButtonDownEvent, self._handle_buttondown, self.app)
      self._callback(self.rgb)

      assert self.app.sequence_pos >= 0
      assert self.app.sequence_pos < len(self.app.sequence)
    else:
      print("unhandled button event in ColourPicker - ignoring")

