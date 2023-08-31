#!/bin/python3

import RPi.GPIO as GPIO
import time
import math

BUZZER_PIN = 13
BUTTON_PIN = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

global p
p = GPIO.PWM(BUZZER_PIN,1)
p.start(0)

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        p.start(50)
        for x in range(0,361):
            sinVal = math.sin(x*(math.pi/360))
            toneVal = 500 + sinVal*200
            p.ChangeFrequency(toneVal)
            time.sleep(0.001)
            print('on')
    else:
        p.stop()
        print('off')
        


GPIO.cleanup()

