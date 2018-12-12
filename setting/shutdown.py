#!/usr/bin/env python

import RPi.GPIO as GPIO
import os, time

GPIO.setmode(GPIO.BCM)

# GPIO19 : reset button
GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# GPIO26 : shutdown button
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def shutdown(channel):
  os.system("sudo shutdown -h now")

def reboot(channel):
  os.system("sudo reboot")

GPIO.add_event_detect(26, GPIO.FALLING, callback = shutdown, bouncetime = 2000)
GPIO.add_event_detect(19, GPIO.FALLING, callback = reboot, bouncetime = 2000)

while 1:
  time.sleep(100)