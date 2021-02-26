# Make morse go flash

# import RPi.GPIO as GPIO
from time import sleep
from morse import *

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(17, GPIO.OUT)

# List of timings
dot = 0.1  # default time
symbol = dot
dash = 3 * dot
word = 7 * dot - 2 * symbol
letter = 3 * dot - 2 * symbol


def theleds(thelist):
    for i in thelist:
        if i == 's':
            #print("dot")
            GPIO.output(18, True)
            sleep(dot)
            GPIO.output(18, False)
        elif i == 'l':
            #print("dash")
            GPIO.output(18, True)
            sleep(dash)
            GPIO.output(18, False)
        elif i == 'y':
            #print('letter')
            sleep(letter)
        else:
            #print("word")
            sleep(word)
        #print("symbol")
        sleep(symbol)
    GPIO.cleanup()  # cleanup all GPIO


def main():
    phrase = str(input("What phrase?\n")).lower()
    phraselist = textmorse(phrase)
    charlist = texttosymb(phraselist)
    #print(phraselist)
    #print(charlist)
    theleds(charlist)


# GPIO.output(17, True)  # example
# GPIO.output(18, False)  # example


# GPIO.cleanup() # cleanup all GPIO


if __name__ == "__main__":
    main()
