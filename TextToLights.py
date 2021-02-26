# Make morse go flash

import RPi.GPIO as GPIO
from time import sleep
from morse import *

# Sets up LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)


def theleds(thelist, times):
    for i in thelist:
        if i == '.':  # If dot
            GPIO.output(18, True)
            sleep(times[0])
            GPIO.output(18, False)
        elif i == '-':  # If dash
            GPIO.output(18, True)
            sleep(times[1])
            GPIO.output(18, False)
        elif i == ' ':  # If space
            sleep(times[3])
        else:  # If slash
            sleep(times[4])
        sleep(times[2])  # Space between characters
    GPIO.cleanup()  # cleanup all GPIO


def main():
    phrase = str(input("What phrase?\n")).lower()  # Requests phrase
    dot = float(input("How long for a dot? (seconds)\n"))  # Requests length of dot
    phraselist = textmorse(phrase)  # Converts phrase using dictionary to morse list
    charlist = texttomorse(phraselist)  # Converts morse list to character list
    timings = timingWindows(dot)  # Generate timings
    theleds(charlist, timings)  # Converts character list to lights


if __name__ == "__main__":
    main()
