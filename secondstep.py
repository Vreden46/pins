#!/bin/python3

import RPi.GPIO as GPIO
import time

LED_PIN = 17

state = input("Bitte geben Sie eine Zahl (0 oder 1) ein: ")
# Eingabe in eine Integer-Zahl umwandeln
try:
    state = int(state)
except ValueError:
    print("Ungültige Eingabe. Bitte geben Sie nur 0 oder 1 ein.")
    exit()

# Überprüfen, ob die Eingabe 0 oder 1 ist
if state != 0 and state != 1:
    print("Die eingegebene Zahl ist weder 0 noch 1.")
    exit()




GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

if state == 1:
    GPIO.output(LED_PIN, GPIO.HIGH)
else:
    GPIO.output(LED_PIN, GPIO.LOW)

time.sleep(2)
GPIO.cleanup()

