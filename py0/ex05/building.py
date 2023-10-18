#!/usr/bin/env python3

import sys


def text_analyser(text: str):
    """
    this program analyse a text and its types of characters
    """
    nbchar = len(text)
    nbupper = sum(character.isupper() for character in text)
    nblower = sum(character.islower() for character in text)
    nbspace = sum(character.isspace() for character in text)
    nbdigit = sum(character.isdigit() for character in text)
    nbpunctuation = nbchar - nbupper - nblower - nbspace - nbdigit
    if nbchar == 1:
        print("the teste contains one character:")
    else:
        print("the teste contains ", nbchar, " characters:")
    if nbupper == 0 or nbupper == 1:
        print(nbupper, " upper letter")
    else:
        print(nbupper, " upper letters")
    if nblower == 0 or nblower == 1:
        print(nblower, " lower letter")
    else:
        print(nblower, " lower letters")
    if nbpunctuation == 0 or nbpunctuation == 1:
        print(nbpunctuation, " punctuation mark")
    else:
        print(nbpunctuation, " punctuation marks")
    if nbspace == 0 or nbspace == 1:
        print(nbspace, " space")
    else:
        print(nbspace, " spaces")
    if nbdigit == 0 or nbdigit == 1:
        print(nbdigit, " digit")
    else:
        print(nbdigit, " digits")


def main():
    """
    this program checks if a text is giver and then analyse it
    and its types of characters
    """
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) < 2:
            user_input = ""
            while not user_input:
                print("Aucun argument n'a été fourni. Veuillez en taper un :")
                user_input = input()
        else:
            user_input = sys.argv[1]
        text_analyser(user_input)
    except AssertionError as msg:
        print("AssertionError: ", str(msg))


if __name__ == "__main__":
    main()
