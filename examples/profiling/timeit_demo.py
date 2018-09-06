# -*- coding: utf-8 -*-

import timeit

"""
>>> t = timeit.Timer("<the-statement-to-timeit>",
                 "<importing modules to help setup the necessary env>")

# Calls my timed statement 1 million times
# and returns number of seconds it took to do it.
>>> t.timeit()

# returns a list of every iteration
>>> t.repeat(<number to repeat>,
             <number of times to call the timed statement>")

# example of repeat
t.repeat(3, 1000000)

# take the min of those 3 iteration
min(t.repeat(3, 1000000))

"""

import string, re

charToSoundex = {"A": "9",
                 "B": "1",
                 "C": "2",
                 "D": "3",
                 "E": "9",
                 "F": "1",
                 "G": "2",
                 "H": "9",
                 "I": "9",
                 "J": "2",
                 "K": "2",
                 "L": "4",
                 "M": "5",
                 "N": "5",
                 "O": "9",
                 "P": "1",
                 "Q": "2",
                 "R": "6",
                 "S": "2",
                 "T": "3",
                 "U": "9",
                 "V": "1",
                 "W": "9",
                 "X": "2",
                 "Y": "9",
                 "Z": "2"}

isOnlyChars = re.compile('^[a-zA-Z]+$').search


def soundex(source):
    "convert string to soundex equivalent"

    # Soundex requirements:
    # source string must be at least 1 character
    # and must consist entirely of letters

    allchars = "".join([string.ascii_uppercase,
                        string.ascii_lowercase])
    if not isOnlyChars(source):
        return "0000"

    # Soundex algorithm:
    # 1. make first character uppercase
    source = source.upper()

    # 2. translate all other characters to soundex digits
    digits = source[0]

    for s in source[1:]:
        digits += charToSoundex[s]

    # 3. remove consecutive duplicates
    digits2 = digits[0]
    for d in digits[1:]:
        if digits2[-1] != d:
            digits2 += d

    # 4. remove all "9"s
    digits3 = re.sub('9', '', digits2)

    # 5. pad end with "0"s to 4 characters
    while len(digits3) < 4:
        digits3 += "0"

    # 6. return first 4 characters
    return digits3[:4]


if __name__ == "__main__":
    from timeit import Timer

    names = ("Woo",
             "Pilgrim",
             "Flingjingwaller")

    for name in names:
        statement = f"soundex('{name}')"
        t = Timer(statement, "from __main__ import soundex")
        print(name.ljust(15, '-'),
              soundex(name),
              min(t.repeat()))


    """
    Woo------------ W000 4.418337304001398
    Pilgrim-------- P426 5.009230576999471
    Flingjingwaller F452 6.995747596000001
    """