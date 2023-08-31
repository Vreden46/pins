#!/bin/python3

import RPi.GPIO as GPIO
import time

LED_PIN = 17
BUTTON_PIN = 26




GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

while True:
    print(GPIO.input(BUTTON_PIN))
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)



GPIO.cleanup()

