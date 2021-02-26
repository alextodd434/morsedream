# Module for Morse Project

# Dictionary
MorseCodes = {
    ' ': '',
    'a': 'sl',
    'b': 'lsss',
    'c': 'lsls',
    'd': 'lss',
    'e': 's',
    'f': 'ssls',
    'g': 'lls',
    'h': 'ssss',
    'i': 'ss',
    'j': 'slll',
    'k': 'lsl',
    'l': 'slss',
    'm': 'll',
    'n': 'ls',
    'o': 'lll',
    'p': 'slls',
    'q': 'llsl',
    'r': 'sls',
    's': 'sss',
    't': 'l',
    'u': 'ssl',
    'v': 'sssl',
    'w': 'sll',
    'x': 'lssl',
    'y': 'lsll',
    'z': 'llss',
    '1': 'sllll',
    '2': 'sslll',
    '3': 'sssll',
    '4': 'ssssl',
    '5': 'sssss',
    '6': 'lssss',
    '7': 'llsss',
    '8': 'lllss',
    '9': 'lllls',
    '0': 'lllll'}


def textmorse(text):
    morse = []
    for t in text:
        if t == ' ':
            morse.pop()
            morse.append('x')
        else:
            morse.append(MorseCodes[t])
            morse.append('y')
        # y gap between letters
    return morse


def texttosymb(morselist):
    symblist = []
    for m in morselist:
        for symbol in m:
            symblist.append(symbol)
    return symblist

