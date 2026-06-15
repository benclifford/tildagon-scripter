from .steps.base import EndStep
from .steps.button import WhenButtonPushedStep
from .steps.count import CountLoopsStep
from .steps.forever import RepeatForeverStep
from .steps.imu import WhenIMUUpright
from .steps.led import LEDStep
from .steps.pause import PauseStep
from .steps.whenplay import WhenPlayStep

def default_program(app):
  return [WhenButtonPushedStep(app),
            LEDStep(255,255,255),
            PauseStep(500),
            LEDStep(0,0,255),
            PauseStep(500),
          EndStep(),

          WhenPlayStep(),
            RepeatForeverStep(),
              LEDStep(255,0,0),
              PauseStep(500),
              LEDStep(0,0,0),
              PauseStep(500),
            EndStep(),
          EndStep(),

          WhenIMUUpright(),
            LEDStep(0,255,0),
          EndStep(),
          ]
