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

#Drivetrain
motor1 = Motor(Ports.PORT19)
motor2 = Motor(Ports.PORT13)

#Group ( Drivetrain )
motor3 = MotorGroup(motor1, motor2)
drivetrain = DriveTrain(motor1, motor2, 259)

#Thinggy
lever = Motor(Ports.PORT10)
roller = Motor(Ports.PORT12)
pneumatics1 = Pneumatics(brain.three_wire_port.a)

#Group (Lever and roller)
motor4 = MotorGroup(lever, roller)

# We don't use this right now
pinchers = Motor(Ports.PORT1)

# For Drivers

def driver_control():
    while True:
        motor2.spin(
            DirectionType.REVERSE,
            controller.axis3.position() + controller.axis1.position(),
            VelocityUnits.PERCENT)
        motor1.spin(
            DirectionType.REVERSE,
            controller.axis3.position() - controller.axis1.position(),
            VelocityUnits.PERCENT)
        
        #Drivetrain
        #Remember: if,elif,else
        
        if controller.buttonR1.pressing():
            motor3.spin(FORWARD, 100, RPM)
    
        
        elif controller.buttonR2.pressing():
            motor3.spin(REVERSE, 100, RPM)

        else:
            motor3.stop()
       

       ##CHANGE L1 and button A!!! 
        if controller.buttonL1.pressing():
            motor3.spin(FORWARD, 20)  
        elif controller.buttonL2.pressing():
            motor3.spin(REVERSE, 20)
        else:
            motor3.stop()

        #Others
        if controller.buttonA.pressing():
            motor4.spin(FORWARD, 100, RPM)
        else:
            motor4.stop()

        if controller.buttonB.pressing():
            pneumatics1.open()
        else:
            pneumatics1.close

# AUTO

def move(distence: DirectionType.DirectionType, distance: int):
    drivetrain.drive_for(distence, distance, MM, velocity=50)


def Auto():
    while True:
       
        drivetrain.turn(RIGHT, 45)
        motor3.spin_for(FORWARD, 13, TURNS)        
        lever.spin(FORWARD, 80, RPM)

if COMPETITION_MODE:
    Competition(driver_control, Auto)

