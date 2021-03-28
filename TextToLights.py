# Turn text input to morse code light flash on Raspberry Pi

import RPi.GPIO as GPIO
from time import sleep
from morse_functions import *

# Sets up LEDs
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)


# Takes in morse character list and required times for characters
def LEDs(character_list, times):
    for i in character_list:
        if i == '.':        # If dot
            GPIO.output(18, True)
            sleep(times[0])
            GPIO.output(18, False)
        elif i == '-':      # If dash
            GPIO.output(18, True)
            sleep(times[1])
            GPIO.output(18, False)
        elif i == ' ':      # If space
            sleep(times[3])
        else:               # If slash
            sleep(times[4])
        sleep(times[2])     # Space between characters
    GPIO.cleanup()          # cleanup all GPIO


def main():
    phrase = str(input("What phrase?\n")).lower()           # Requests phrase
    dot = float(input("How long for a dot? (seconds)\n"))   # Requests length of dot
    phrase_list = text_morse(phrase)                        # Converts phrase using dictionary to morse list
    char_list = text_to_morse(phrase_list)                  # Converts morse list to character list
    timings = timing_windows(dot)                           # Generate timings for morse characters
    LEDs(char_list, timings)                                # Converts character list to lights


if __name__ == "__main__":
    main()
