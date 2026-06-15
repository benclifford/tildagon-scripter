import power

from .base import EndStep, WhenStep
from ..const import LIVE_SIZE, EDIT_MODE

# As "whens"...
# TODO: battery full
# TODO: battery empty
# TODO: power connected
# TODO: power disconnected
# and maybe later as bools?


class WhenHysteresisStep(WhenStep):
  def __init__(self, *, high: float, low: float, text: str):
    super().__init__()
    # This is factored hysteresis code for battery checking but
    # it should be usable for any value-hysteresis kind of
    # when block, I think (see how its like IMU code)
    self.last_state = False  # False is "not triggered" - TODO: should start at current value.
    self.low = low
    self.high = high
    self.text = text

  def poll_value(self):
    raise RuntimeError("You need to override this with own measurement")

  def poll_for_when(self):
    next_value = self.poll_value()
    if next_value < self.low:
      next_state = False
    elif next_value > self.high:
      next_state = True
    else:
      next_state = self.last_state
      # in the middle hysteresis range, don't change state

    if self.last_state == False and next_state == True:
      trigger = True
    else:
      trigger = False

    self.last_state = next_state

    return trigger

  def progress_step(self):
    return False

  def render(self, mode, ctx, render_step, y, text_colour):
    tw = ctx.text_width(self.text)
    ctx.move_to(int(-tw/2), y).rgb(*text_colour).text(self.text)
    ctx.rgb(255,0,0).begin_path()
    ctx.move_to(-240, y - LIVE_SIZE/2)
    ctx.line_to(240, y - LIVE_SIZE/2)
    ctx.stroke()


class WhenPowerConnected(WhenHysteresisStep):
  def __init__(self):
    super().__init__(high=4.5, low=3, text="When power connected")

  def poll_value(self):
    return power.Vin()


class InsertPowerConnected:

  name = "When power connected"

  def __init__(self, app):
    self.app = app

  def update(self, delta):
    """This is a WhenStep so the insert should happen at the end of the program, as a new top level block."""
    self.app.sequence.append(WhenPowerConnected())
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


class WhenBatteryFull(WhenHysteresisStep):
  def __init__(self):
    super().__init__(high=0.98, low=0.96, text="When battery full")

  def poll_value(self):
    return power.BatteryLevel()


class InsertBatteryFull:

  name = "When battery full"

  def __init__(self, app):
    self.app = app

  def update(self, delta):
    """This is a WhenStep so the insert should happen at the end of the program, as a new top level block."""
    self.app.sequence.append(WhenBatteryFull())
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
