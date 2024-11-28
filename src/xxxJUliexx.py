
# Library imports
from vex import *
import math

# Brain should be defined by default

brain = Brain()
DriveTrain = DriveTrain
controller = Controller()
pneumatics= Pneumatics


brain.screen.print("Hell00000")

motor1 = Motor(Ports.PORT20)
motor2 = Motor(Ports.PORT11)
pneumatics1=Pneumatics(brain.three_wire_port.a)




motor = MotorGroup(motor1, motor2)

# DONE
lever = Motor(Ports.PORT10)


# DONE
pinchers = Motor(Ports.PORT1)


def driver_control():
  while True:
      if controller.buttonR1.pressing():
            motor1.spin(DirectionType.FORWARD, 100, RPM)
      else:
          motor1.stop(BRAKE)
      if controller.buttonL1.pressing():
            motor2.spin(DirectionType.FORWARD, 100, RPM)  
      else:
          motor2.stop(BRAKE)
      if controller.buttonA.pressing():
          pneumatics1.open()
      else:pneumatics1.close
      if controller.buttonB.pressing():
          pinchers.spin(FORWARD,80,RPM)
      else: pinchers.stop(BRAKE)
      if controller.buttonX.pressing():
          pinchers.spin(REVERSE,80,RPM)
      else: pinchers.stop(BRAKE)
      
        
driver_control()




