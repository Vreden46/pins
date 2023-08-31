#!/bin/python3

import RPi.GPIO as GPIO
import time
import math
import random

BUZZER_PIN = 13
BUTTON_PIN = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

global p
p = GPIO.PWM(BUZZER_PIN,0.5)
p.start(0)

while True:
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        p.start(50)
        base_frequency = 1000
        frequency_offset = random.uniform(-300, 300)
        tone_val = base_frequency + frequency_offset
        p.ChangeFrequency(tone_val)
        time.sleep(0.05)
        print('on')
    else:
        p.stop()
        print('off')
        


GPIO.cleanup()

