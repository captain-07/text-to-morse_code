text = input("Enter your text: ").upper()
MORSE_CODE_DIC = {
    # Letters (A-Z)
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': ' ',

    # Numbers (0-9)
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    # Official ITU Punctuation & Signs
    '.': '.-.-.-',  # Full stop (period)
    ',': '--..--',  # Comma
    ':': '---...',  # Colon or division sign
    '?': '..--..',  # Question mark
    "'": '.----.',  # Apostrophe
    '-': '-....-',  # Hyphen or dash
    '/': '-..-.',  # Fraction bar
    '(': '-.--.',  # Parenthesis (left)
    ')': '-.--.-',  # Parenthesis (right)
    '"': '.-..-.',  # Inverted commas (quotation marks)
    '=': '-...-',  # Double dash (Equal sign)
    '+': '.-.-.',  # Cross (Plus sign)
    '@': '.--.-.',  # Commercial at (Arobase)

    # Accented Letters (The only one explicitly in ITU-R M.1677-1)
    'É': '..-..'
}
def text_to_morse(a):
    list_of_text = list(a)
    list_of_morse = []
    for char in list_of_text:
        list_of_morse.append(MORSE_CODE_DIC[char])
        list_of_morse.append(' ')
    morse_code = ''.join(list_of_morse)
    return morse_code

print("Your morse code is: ",text_to_morse(text))