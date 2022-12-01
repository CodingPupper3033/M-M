#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *

#Initializing motors
#motorLeft = LargeMotor('outA'); motorLeft.stop_action = 'hold'
#motorRight = LargeMotor('outD'); motorRight.stop_action = 'hold'

#Constants
_rotateErrorMargin = 2; # How close to an angle the robot has to be to declare it "good enough"
_rotateSpeedMultiplier = 1; # How touchy the speed of the motor will be. Higher, the more "jerky" the motor will be

tempI = 0;
tempMax = 90;
rotateAngle = 90;

def rotateTo(angle):
    angle = restrictAngle180(angle)
    
    angleLast = restrictAngle180(getGyroAngle())
    difference = restrictAngle180(angle-angleLast);
    while (abs(difference) > _rotateErrorMargin):
        mototPower = math.sin(math.radians(difference/2)) # Restricts Power to be between -1 and 1
        

        angleLast = restrictAngle180(getGyroAngle())
        difference = restrictAngle180(angle-angleLast);

def rotate(angle):
    rotateTo(getGyroAngle()+angle)

def rotateToDirection(direction): # 1 - North, 2 - East, 3 - South, 4 - West
    rotateTo((direction-1)*90)

def rotateDirection(direction): # 1 - Nothing, 2 - East, 3 - South, 4 - West
    rotate((direction-1)*90)

def getGyroAngle():
    global tempI
    if tempI == 0:
        out = tempMax+rotateAngle
        tempI+=1
    else:
        out = (tempMax*math.sin(tempI)/tempI)+rotateAngle
        tempI+=1
    return out
    
def restrictAngle180(x):
    return ((x + 180) % 360) - 180

rotateDirection(4)