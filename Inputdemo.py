#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')
#Initializing motors
motorLeft = LargeMotor('outA'); motorLeft.stop_action = 'hold'
motorRight = LargeMotor('outD'); motorRight.stop_action = 'hold'

#Initializing lightsensors
leftSensor = ColorSensor(INPUT_1)
rightSensor = ColorSensor(INPUT_4)

#function syntax
def rotate(multiplier):
    #rotate
    motorLeft.run_to_rel_pos(position_sp= 1 * multiplier, speed_sp = 250)
    motorRight.run_to_rel_pos(position_sp= -1 * multiplier, speed_sp = 250)
    # pause the program while motors are running
    motorLeft.wait_while('running')
    motorRight.wait_while('running')
    #linear movement
    motorLeft.run_to_rel_pos(position_sp= multiplier / 2, speed_sp = 250)
    motorRight.run_to_rel_pos(position_sp= multiplier / 2, speed_sp = 250)
    # pause the program while motors are running
    motorLeft.wait_while('running')
    motorRight.wait_while('running')
    return leftSensor.reflected_light_intensity, rightSensor.reflected_light_intensity

#If you want your robot to make sounds!
sound = Sound()
print('Hello, my name is EV3!')

#text to speech
sound.speak('Hello, my name is E V 3!')

sleep(1)


# empty list
intensities = []

#loop 5 times
for i in range(5):
    # take user input as an integer
    value = int(input("Give me a positive or negative number: "))

    #add light values to list
    intensities.append(rotate(value))

for i in range(len(intensities)):
    # print each intensity tuple
    print(intensities[i])

sleep(5)
