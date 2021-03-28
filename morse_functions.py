# Module for Morse Functions within Morse Project

# Dictionary of letters to morse
morseDictionary = {
    '/': ' ',
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
unmorseDictionary = {value: key for key, value in morseDictionary.items()}


# Converts letters using dictionary
def text_morse(text):
    morse = []
    for t in text:
        if t == ' ':  # Converts space to /
            morse.pop()  # Removes space between characters
            morse.append(morseDictionary[t])  # Appends / to dictionary list
        else:
            morse.append(morseDictionary[t])  # Appends dictionary conversion
            morse.append(' ')  # Appends space after character
        # y gap between letters
    return morse


# Converts letters to morse . and -
def text_to_morse(morse_list):
    symb_list = []
    for m in morse_list:
        for symbol in m:
            symb_list.append(symbol)  # Converts dictionary list into list of characters
    return symb_list


# Converts morse . and - to letters
def morse_to_text(morse_code):
    sentence = []
    for t in range(2, len(morse_code)):
        if t == "":
            pass
        else:
            try:
                sentence.append(unmorseDictionary[morse_code[t]])
            except KeyError:
                pass
    sentence = "".join(sentence)
    sentence = sentence.replace('/', '')
    return sentence


# Defines timing windows for Morse code
def timing_windows(dot):
    symbol = dot
    dash = 3 * dot
    word = 7 * dot - 2 * symbol
    letter = 3 * dot - 2 * symbol
    return [dot, dash, symbol, letter, word]


# Warning to confirm if functions file was run independently
def main():
    print("Have you run the correct file?")


if __name__ == "__main__":
    main()
