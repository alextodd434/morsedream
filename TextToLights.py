# Make morse go flash

# import RPi.GPIO as GPIO
from time import sleep
from morse import *

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(18, GPIO.OUT)
# GPIO.setup(17, GPIO.OUT)

# List of timings
dot = 0.1  # default time
dash = 3 * dot
word = 7 * dot
letter = 3 * dot
symbol = dot


def theleds(thelist):
    for i in thelist:
        if i == 's':
            print("dot")
            sleep(dot)
            print("symbol")
            sleep(symbol)
        elif i == 'l':
            print("dash")
            sleep(dash)
            print("symbol")
            sleep(symbol)
        elif i == 'y':
            print('letter')
            sleep(letter)
        else:
            print("word")
            sleep(word)


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
