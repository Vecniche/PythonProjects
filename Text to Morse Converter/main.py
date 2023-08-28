morse_code_dict = {

    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',

    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',

    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',

    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',

    '7': '--...', '8': '---..', '9': '----.'

}


def text_to_morse_converter(text):
    morse_code = []
    for char in text.upper():
        if char == ' ':
            morse_code.append()

        elif char in morse_code_dict:
            morse_code.append(morse_code_dict[char])

    return ' '.join(morse_code)

text_input = input("Enter the Text you will like to convert to morse code: ")
morse_result = text_to_morse_converter(text_input)
print(text_input, morse_result)


