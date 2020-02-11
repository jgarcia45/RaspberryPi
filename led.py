#First Program
#Created on August 25, 2016
#Understanding Python and Using GPIO Pins on Raspberry Pi

import time
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
for i in range(0, 5):
  time.sleep(2)
  print ("LED on")
  GPIO.output(17, GPIO.HIGH)
  time.sleep(1)
  print ("LED off")
  GPIO.output(17, GPIO.LOW)
