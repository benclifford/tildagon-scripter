from .base import Step

class CountLoopsStep(Step):
  def __init__(self):
    self.reset()

  def enter_step(self):
    self.count += 1

  def render(self, mode, ctx, render_step, y, text_colour):
    text = f"{render_step}: Counted {self.count} times"
    tw = ctx.text_width(text)
    ctx.move_to(int(-tw/2), y).rgb(*text_colour).text(text)

  def reset(self):
    self.count = 0
