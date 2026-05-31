from .base import EndStep, WhenStep
from ..const import LIVE_SIZE, EDIT_MODE

class WhenPlayStep(WhenStep):

  def __init__(self):
    super().__init__()
    self._start = False

  def poll_for_when(self):
    if self._start:
      self._start = False
      return True
    else:
      return False

  def progress_step(self):
    return False

  def render(self, mode, ctx, render_step, y, text_colour):
    text = f"When play starts"  # : {self._start}"
    tw = ctx.text_width(text)
    ctx.move_to(int(-tw/2), y).rgb(*text_colour).text(text)
    ctx.rgb(255,0,0).begin_path()
    ctx.move_to(-240, y - LIVE_SIZE/2)
    ctx.line_to(240, y - LIVE_SIZE/2)
    ctx.stroke()

  def reset(self):
    self._start = True


class InsertWhenPlayStepUI:
  def __init__(self, app):
    self.app = app

  def update(self, delta):
    """This is a WhenStep so the insert should happen at the end of the program, as a new top level block."""
    self.app.sequence.append(WhenPlayStep())
    self.app.sequence.append(EndStep())

    # move cursor to end step so that a subsequent InsertStep will populate the new when block
    self.app.sequence_pos = len(self.app.sequence) - 1

    assert self.app.sequence_pos >= 0
    assert self.app.sequence_pos < len(self.app.sequence)

    # this will make the end step be populated properly
    # which won't happen otherwise.
    # TODO: maybe steps (aka step authors) shouldn't be
    # responsible for this and I can make it happen when
    # going back to one of the framework modes?
    self.app._reset_steps()

    # and remove ourselves from the app
    self.app.ui_delegate = None
    self.app._mode = EDIT_MODE

  def draw(self, ctx):
    pass
