#!/bin/python3

import RPi.GPIO as GPIO
import time

LED_PIN = 17
zaehler = 10

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)







GPIO.cleanup()

