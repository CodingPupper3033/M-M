#!/usr/bin/env python3

import os
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

#Constants
#Rotation
_rotateErrorMargin = 0.5; # How close to an angle the robot has to be to declare it "good enough"
_rotateSpeedMultiplier = 1; # How touchy the speed of the motor will be. Higher, the more "jerky" the motor will be

#Initializing motors
motorLeft = LargeMotor('outA'); motorLeft.stop_action = 'hold'
motorRight = LargeMotor('outB'); motorRight.stop_action = 'hold'

os.system('setfont Lat15-TerminusBold14')

#Initializing sensors
gyroSensor = GyroSensor(INPUT_3)

def rotateTo(angle): # Rotates to a specified angle
    print("Rotating to angle: %d"%angle)
    angle = restrictAngle180(angle)
    
    angleLast = restrictAngle180(getGyroAngle())
    difference = restrictAngle180(angleLast-angle);
    while (abs(difference) > _rotateErrorMargin):
        motorPower = math.sin(math.radians(difference/2)) # Restricts Power to be between -1 and 1
        motorPower *= _rotateSpeedMultiplier # Speed change by the multiplier

        maxSpeed = min(motorLeft.max_speed,motorRight.max_speed) #Max speed of the slowest motor

        motorSpeed = maxSpeed*motorPower # Speed for the motor to go

        motorLeft.run_forever(speed_sp = -motorSpeed)
        motorRight.run_forever(speed_sp = motorSpeed)


        angleLast = restrictAngle180(getGyroAngle())
        difference = restrictAngle180(angleLast-angle);
    motorLeft.stop()
    motorRight.stop()
    print("Rotated to angle: %d"%getGyroAngle())

def rotate(angle): #Changes the current angle by the variable angle 
    rotateTo(getGyroAngle()+angle)

def rotateToDirection(direction): #Rotates to direction: 1 - North, 2 - East, 3 - South, 4 - West
    rotateTo(((direction-1)%4)*90)

def rotateDirection(direction): # Rotates from the current position to the: 1 - Nothing, 2 - Right, 3 - Back, 4 - Left
    rotate(((direction-1)%4)*90)

def getGyroAngle():
    return -gyroSensor.angle
    
def restrictAngle180(x):
    return ((x + 180) % 360) - 180

gyroSensor.reset() # Resets the gyro to have north be the direction we were when we started 