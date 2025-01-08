# ---------------------------------------------------------------------------- #
#                                                                              #
#   Module:       main.py                                                      #
#   Author:       REBECCA HALE                                                 #
#   Created:      11/21/2023, 5:01:50 PM                                       #
#   Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #


# Library imports

from vex import *
import math
COMPETITION_MODE = True


# Brain should be defined by default

brain = Brain()
DriveTrain = DriveTrain
controller = Controller()

# Drivetrain ( motor1= left, motor2= right)
motor1 = Motor(Ports.PORT13)
motor2 = Motor(Ports.PORT19, True)

# Others
pneumatics1 = Pneumatics(brain.three_wire_port.a)

lever = Motor(Ports.PORT14)
roller = Motor(Ports.PORT15)


# Group ( Drivetrain )
drivetrain = DriveTrain(motor1, motor2, 259)
# auto drive
gyro = Gyro(brain.three_wire_port.f)
autodrive = SmartDrive(motor1, motor2, gyro, 255)


# Group (Lever and roller)
icecream = MotorGroup(lever, roller)


# For Drivers

def driver_control():

    state = 1

    lastpressed = False
    lastpressed2 = False

    while True:

        # Drivetrain
        axis3 = controller.axis3.position()
        axis1 = controller.axis1.position()

        if -10 < axis3 < 10:
            axis3 = 0

        if -10 < axis1 < 10:
            axis1 = 0

        if axis1 == 0 or axis3 == 0:
            drivetrain.stop

        motor1.spin(
            DirectionType.FORWARD, axis3-axis1, VelocityUnits.PERCENT)

        motor2.spin(
            DirectionType.FORWARD, axis3+axis1, VelocityUnits.PERCENT)

        # Penumatics

        if controller.buttonB.pressing():
            pneumatics1.open()

        else:
            pneumatics1.close()

        # Lever and roller

        if state == 1:
            icecream.stop()
        elif state == 2:
            icecream.spin(DirectionType.FORWARD, 100, PERCENT)
        elif state == 3:
            icecream.spin(DirectionType.REVERSE, 100, PERCENT)

        # Right side for lever and roller
        if state == 1 and controller.buttonR1.pressing():
            state = 3
            lastpressed2 = True

        elif state == 3 and controller.buttonR1.pressing():
            state = 1
            lastpressed2 = False

        elif state == 2 and controller.buttonR1.pressing():
            state = 3
            lastpressed2 = True

        elif state == 3 and controller.buttonL1.pressing():
            state = 2
            lastpressed = True

        elif state == 1 and controller.buttonL1.pressing():
            state = 2
            lastpressed = True

        elif state == 2 and controller.buttonL1.pressing():
            state = 1
            lastpressed2 = False
        if lastpressed or lastpressed2 is not controller.buttonR1.pressing():
            pass

        # lever and roller

        if state == 1:
            icecream.stop()
        elif state == 2:
            icecream.spin(DirectionType.FORWARD, 100, PERCENT)
        elif state == 3:
            icecream.spin(DirectionType.REVERSE, 100, PERCENT)

        wait(10)

        lastpressed = controller.buttonR1.pressing()
        lastpressed2 = controller.buttonL1.pressing()

# AUTO


def move(distence: DirectionType.DirectionType, distance: int):
    drivetrain.drive_for(distence, distance, MM, velocity=50)


def auto():
    while True:

        autodrive.turn(RIGHT, 45)
        autodrive.drive_for(FORWARD, 800, MM)
        lever.spin(FORWARD, 255, RPM)
        wait(100)
        lever.stop()


if COMPETITION_MODE:
    Competition(driver_control, auto)
else:
    driver_control()
