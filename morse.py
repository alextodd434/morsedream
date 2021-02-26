# Module for Morse Project

# Dictionary
MorseCodes = {
    ' ': '/',
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'}


# Reads backwards dictionary
unmorse = {value: key for key, value in MorseCodes.items()}


# Converts letters using dictionary
def textmorse(text):
    morse = []
    for t in text:
        if t == ' ':  # Converts space to /
            morse.pop()  # Removes space between characters
            morse.append(MorseCodes[t])  # Appends / to dictionary list
        else:
            morse.append(MorseCodes[t])  # Appends dictionary conversion
            morse.append(' ')  # Appends space after character
        # y gap between letters
    return morse


def texttomorse(morselist):
    symblist = []
    for m in morselist:
        for symbol in m:
            symblist.append(symbol)  # Converts dictionary list into list of characters
    return symblist


def morsetotext(morsecode):
    sentence = []
    test = morsecode.split()
    print(test)
    for t in test:
        sentence.append(unmorse[t])
    return sentence


def timingWindows(dot):
    symbol = dot
    dash = 3 * dot
    word = 7 * dot - 2 * symbol
    letter = 3 * dot - 2 * symbol
    return [dot, dash, symbol, letter, word]

#morsetotext('.... .. / .--- .- -.- .')
