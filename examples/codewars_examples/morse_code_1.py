MORSE_CODE = {}
CHAR_SEP = ' '
WORD_SEP = ' ' * 3


def decode_morse(morse_code):
    return ' '.join([''.join(['A' for i in m.split(CHAR_SEP)])for m in (morse_code.strip()).split(WORD_SEP)])


decode_morse('.... . -.--   .--- ..- -.. .')
