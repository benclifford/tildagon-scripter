from tildagonos import tildagonos

from .base import Step


class LEDStep(Step):
  def __init__(self, r, g, b):
    self.rgb = (r, g, b)
    self.leds = list(range(0,12)) # all LEDs

  def enter_step(self):

    colour = self.rgb
    for n in self.leds:
      tildagonos.leds[n+1] = colour
    tildagonos.leds.write()

  def render(self, mode, ctx, render_step, y, text_colour):
    text = f"{render_step}: Set LEDs to "
    tw = ctx.text_width(text)
    tw2 = ctx.text_width("this colour")
    w = tw + tw2
    this_colour = (self.rgb[0] / 256, self.rgb[1] / 256, self.rgb[2] / 256)
    ctx.move_to(int(-w/2), y).rgb(*text_colour).text(text)
    ctx.move_to(int(-w/2 + tw), y).rgb(*this_colour).text("this colour")
