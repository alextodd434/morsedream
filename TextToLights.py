# Make morse go flash

import RPi.GPIO as GPIO
from time import sleep
from morse import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

dot = 0.1
dash = 3 * dot
word = 7 * dot
letter = 3 * dot
symbol = dot




sleep(0.5) # example
GPIO.output(17, True) # example
GPIO.output(18, False) # example










GPIO.cleanup() # cleanup all GPIO 
