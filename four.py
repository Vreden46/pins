#!/bin/python3

import RPi.GPIO as GPIO
import time

LED_PIN = 17
BUTTON_PIN = 26




GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    time.sleep(0.01)
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
   
    



GPIO.cleanup()

