#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sound import Sound
from time import sleep
import os
os.system('setfont Lat15-TerminusBold14')
#Initializing motors
motorLeft = LargeMotor('outB'); motorLeft.stop_action = 'hold'
motorRight = LargeMotor('outC'); motorRight.stop_action = 'hold'
#Uncomment the line below if you want to use the third, smaller, motor for anything
#MM = MediumMotor('outA'); MM.stop_action = 'hold' 

#Initializing lightsensors
leftSensor = ColorSensor(INPUT_2)
rightSensor = ColorSensor(INPUT_3)

#If you want your robot to make sounds!
sound = Sound()

#Setting a black value to compare to. Reflected light intensity returns a number between 0 and 100 -- higher values are brighter, lower values are darker.
leftBlack = leftSensor.reflected_light_intensity
rightBlack = rightSensor.reflected_light_intensity

print('Hello, my name is EV3!')

#text to speech
sound.speak('Hello, my name is E V 3!')

sleep(3)
print('This is a test!')
sleep(3)
#motorLeft.run_to_rel_pos(position_sp= 840, speed_sp = 250)
#motorRight.run_to_rel_pos(position_sp=-840, speed_sp = 250)
#motorLeft.wait_while('running')
#motorRight.wait_while('running')

t = 0
while t <= 30:
    print(leftSensor.reflected_light_intensity, rightSensor.reflected_light_intensity)
    sleep(2)
    t+=1