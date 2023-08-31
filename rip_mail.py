#!/bin/python3

import RPi.GPIO as GPIO
import time
import math
from datetime import datetime

import smtplib
from email.mime.text import MIMEText


BUZZER_PIN = 13
PIR_PIN = 26
buzzer = 0
send = 0

# E-Mail-Verbindung herstellen
smtp_server = 'smtp.1und1.de'
smtp_port = 587
username = 'tv@pro-vreden.de'
password = ''

file_path = '/home/torsten/.local/.mailpw'

try:
    with open(file_path, 'r') as file:
        password = file.read().strip()  # Den Inhalt der Datei lesen und Leerzeichen entfernen
        print("Password:", password)  # Ausgabe des gelesenen Passworts (nur für Testzwecke)
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")
except Exception as e:
    print("Ein Fehler ist aufgetreten:", str(e))



# E-Mail-Inhalt erstellen
sender = 'tv@pro-vreden.de'
recipient = 'tv@pro-vreden.de'
subject = 'Test Email'




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
    send = 0
    if buzzer == 1:
        p.start(50)
        for x in range(0,361):
            sinVal = math.sin(x*(math.pi/360))
            toneVal = 500 + sinVal*200
            p.ChangeFrequency(toneVal)
            current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if send == 0:
                message = f'This is an Alarm-Mail sent at {current_datetime}.'
                msg = MIMEText(message)
                msg['Subject'] = subject
                msg['From'] = sender
                msg['To'] = recipient
                # E-Mail senden
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(username, password)
                server.sendmail(sender, [recipient], msg.as_string())
                # Verbindung beenden
                server.quit()
                print('sended!')
                send = 1
            
            time.sleep(0.001)
            #print('on' + str(current_datetime))
    else:
        p.stop()
        print('off')
        


GPIO.cleanup()

