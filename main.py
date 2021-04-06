import winsound
import time
# Dictionary with letter in morse code
morse_code_dict = {'A': '*-', 'B': '-***', 'C': '-*-*', 'D': '-**', 'E': '*', 'F': '**-*',
                   'G': '--*', 'H': '****', 'I': '**', 'J': '*---',
                   'K': '-*-', 'L': '*-**', 'M': '--', 'N': '-*',
                   'O': '---', 'P': '*--*', 'Q': '--*-', 'R': '*-*',
                   'S': '***', 'T': '-', 'U': '**-', 'V': '***-',
                   'W': '*--', 'X': '-**-', 'Y': '-*--', 'Z': '--**',
                   '1': '*----', '2': '**---', '3': '***--', '4': '****-',
                   '5': '*****', '6': '-****', '7': '--***', '8': '---**',
                   '9': '----*', '0': '-----', '"': '*-**-*', '-': '-****-',
                   '\'': '*----*', '?': '**--**', ':': '---***', ',': '--**--',
                   '.': '*-*-*-', '(': '-*--*-', ')': '-*--*-', ' ': '/'}

# Ask user for sentence
user_input = input('Yooooo, here you can convert any string into Morse Code!!'
                   'Write you sentence and hit ENTER : ')

# Convert into Morse Code
user_sentence_in_morse_code = ' '.join(map(str, [morse_code_dict[letter] for letter in user_input.upper()]))

print(f'MORSE CODE : {user_sentence_in_morse_code}')
print('You can also listen it :) if don\'t want to, RUN!!!')

# We need to replace ' / ' to make pause between words
user_sentence_in_morse_code_for_beep = user_sentence_in_morse_code.replace(' / ', '   ')

# Play our Morse Code
for char in user_sentence_in_morse_code_for_beep:
    if char == '*':
        winsound.Beep(300, 300)
    elif char == '-':
        winsound.Beep(300, 900)
    elif char == ' ':
        time.sleep(0.3)
