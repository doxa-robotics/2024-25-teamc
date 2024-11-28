# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Programer                                                    #
# 	Created:      8/29/2024, 3:48:41 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
import math
from vex import *

# Brain should be defined by default
brain = Brain()

controller = Controller()



DriveTrain = DriveTrain


brain.screen.print("Hello V5")

motor1 = Motor(Ports.PORT1)
motor2 = Motor(Ports.PORT2)
mg1 = MotorGroup(motor1, motor2)


DEBUG = False
#     d1: Defense, push into goal
#     d2: None
#     o1:  match load offense, touch bar
#     o2: don't touch bar
# skills: 60s *auton* skills
#   none: no-op, so do nothing during auton period
AUTON_ROUTINE = "o2"


# Distance between wheel centers, mm
TRACK_WIDTH = 305
# Distance robot moves in one motor turn, mm
TRACK_DISTANCE = 460


def convert_damped_controller(val):
    value = math.pow(0.1*val, 2)
    if val < 0:
        return -value
    else:
        return value

    # Pistons (DONE)
wing_piston = Pneumatics(brain.three_wire_port.a)
balance_piston = Pneumatics(brain.three_wire_port.h)
