#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from time import sleep

import os

from WumpusRotation import rotateToDirection
os.system('setfont Lat15-TerminusBold14')

align_find_line_speed = 25;
align_light_sensor_intensity = 40;
align_motor_sensing_speed = 10
center_align_time_adjustment = 0.75;

#Initializing motors
#CHECK THAT YOUR CHANNELS "outA, outB, outC, outD" ARE CORRECT BEFORE RUNNING
motorLeft = LargeMotor('outA'); motorLeft.stop_action = 'hold'
motorRight = LargeMotor('outB'); motorRight.stop_action = 'hold'
#Uncomment the line below if you want to use the third, smaller, motor for anything
#MM = MediumMotor('outA'); MM.stop_action = 'hold' 

#Initializing lightsensors
leftSensor = ColorSensor(INPUT_1)
rightSensor = ColorSensor(INPUT_2)

def align():
    print("Aligning")

    # Align on line
    while (True):
        if leftSensor.reflected_light_intensity >= align_light_sensor_intensity and rightSensor.reflected_light_intensity >= align_light_sensor_intensity:
            motorLeft.off()
            motorRight.off()
            break
        if (leftSensor.reflected_light_intensity < align_light_sensor_intensity and rightSensor.reflected_light_intensity < align_light_sensor_intensity):
            motorLeft.on(align_find_line_speed)
            motorRight.on(align_find_line_speed)

        else:
            motorLeft.off()
            motorRight.off()
            if leftSensor.reflected_light_intensity < align_light_sensor_intensity: # If left side can't see anything
                motorRight.on(-align_motor_sensing_speed)
            if rightSensor.reflected_light_intensity < align_light_sensor_intensity:
                motorLeft.on(-align_motor_sensing_speed)
    print("Aligned")

def center():
    print("Moving over Line")
    motorLeft.on(align_find_line_speed)
    motorRight.on(align_find_line_speed)

    while (leftSensor.reflected_light_intensity > align_light_sensor_intensity or rightSensor.reflected_light_intensity > align_light_sensor_intensity):
        pass
    motorLeft.stop()
    motorRight.stop()

    print("Centering")
    # Check distance by time
    startTime = time.time()
    motorLeft.on(align_find_line_speed)
    motorRight.on(align_find_line_speed)

    while (leftSensor.reflected_light_intensity < align_light_sensor_intensity and rightSensor.reflected_light_intensity < align_light_sensor_intensity):
        pass
    motorLeft.stop()
    motorRight.stop()
    stopTime = time.time()

    # Go to middle
    timeToCenter = (stopTime-startTime)/2
    centeringTimeStart = time.time()
    motorLeft.on(-align_find_line_speed)
    motorRight.on(-align_find_line_speed)
    
    while (time.time()-centeringTimeStart < timeToCenter+center_align_time_adjustment):
        pass
    motorLeft.stop()
    motorRight.stop()
    print("Centered")

def moveToNextSquare():
    align()
    center()

moveToNextSquare()
rotateToDirection(2)
moveToNextSquare()