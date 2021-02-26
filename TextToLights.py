# Make morse go flash

import RPi.GPIO as GPIO
from time import sleep
from morse import *

# Sets up LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

# List of timings
dot = 0.25  # default time
symbol = dot
dash = 3 * dot
word = 7 * dot - 2 * symbol
letter = 3 * dot - 2 * symbol


def theleds(thelist):
    for i in thelist:
        if i == '.':  # If dot
            GPIO.output(18, True)
            sleep(dot)
            GPIO.output(18, False)
        elif i == '-':  # If dash
            GPIO.output(17, True)
            sleep(dash)
            GPIO.output(17, False)
        elif i == ' ':  # If space
            sleep(letter)
        else:  # If slash
            sleep(word)
        sleep(symbol)  # Space between characters
    GPIO.cleanup()  # cleanup all GPIO


def main():
    phrase = str(input("What phrase?\n")).lower()  # Requests phrase
    phraselist = textmorse(phrase)  # Converts phrase using dictionary to morse list
    charlist = texttomorse(phraselist)  # Converts morse list to character list
    theleds(charlist)  # Converts character list to lights


if __name__ == "__main__":
    main()
