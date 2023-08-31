#!/bin/python3

import RPi.GPIO as GPIO
import time
import math

import smtplib
from email.mime.text import MIMEText


BUZZER_PIN = 13
PIR_PIN = 26
buzzer = 0




GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

global p
p = GPIO.PWM(BUZZER_PIN,1)
p.start(0)

while True:
    time.sleep(0.1)
    print(GPIO.input(PIR_PIN))
    buzzer = GPIO.input(PIR_PIN)
    if buzzer == 1:
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

