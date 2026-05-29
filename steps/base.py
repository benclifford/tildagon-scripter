class Step:
  def __init__(self):
    # Where the step lives inside the program, for referencing.
    # I'd prefer a more object graph style program structure,
    # which would get rid of this field.
    self._step_number: int

  def enter_step(self):
    pass

  def progress_step(self):
    # by default, step finishes immediately, so that one shot steps only
    # need to override enter_step. 
    # return True for "move to next step", False for "stay in this step",
    # or an integer to jump to that step number.
    return True

  def render(self, mode, ctx, render_step, y, text_colour):
    text = f"{render_step}: No description"
    tw = ctx.text_width(text)
    ctx.move_to(int(-tw/2), y).rgb(*text_colour).text(text)

  def poll_for_when(self):
    # If this is a When step that has fired (and so wants to run events),
    # return True (once) and the executor will start running at the
    # step after this one.
    return False

  def reset(self):
    # Called to reset the step, for example when play stops or starts
    pass


# kind of step that pairs with an EndStep to scope out a block of steps
class BlockStep(Step):
    def progress_end_step(self):
        """What to do when the corresponding EndStep is reached."""
        ...

    def get_end_name(self) -> str:
        """Return the name used in end blocks"""
        return "block"

