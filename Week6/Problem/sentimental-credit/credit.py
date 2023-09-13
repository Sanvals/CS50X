# TODO
from cs50 import get_string
import sys


def main():
    card = getcard()

    if luhn(card):
        recognizeCard(card)
    else:
        print("INVALID")


# Get the card number
def getcard():
    # Check the available length
    cardLenghts = [13, 15, 16]
    while True:
        # Get a string of correct size
        card = str(get_string("Number: "))
        if len(card) in cardLenghts:
            return card
        # Or return INVALID and close the program
        else:
            print("INVALID")
            sys.exit(0)


# Build the card identifier
def recognizeCard(string):
    # If it passes the algorythm
    digits = len(string)
    # Check the data for AMEX
    if digits == 15 and string[:2] in ["34", "37"]:
        print("AMEX")
    # Check the data for MASTERCARD
    elif digits == 16 and string[:2] in ["51", "52", "53", "54", "55"]:
        print("MASTERCARD")
    # Check the data for VISA
    elif digits in [13, 16] and string[0] == "4":
        print("VISA")
    else:
        print("INVALID")
        sys.exit(0)


def luhn(card):
    sumA, sumB = 0, 0
    # We jump two spaces from the second to last character
    for i in range(len(str(card)) - 1, 0, -2):
        # And multiply those by 2
        multi = int(str(card[i - 1])) * 2
        # Check if it's > 10
        if multi < 10:
            sumA += multi
        else:
            # And if it is, sum its digits
            sumA += int(str(multi)[0]) + int(str(multi)[1])

    # We jump two spaces from the last character
    for i in range(len(card), 0, -2):
        # And add it to sumB
        sumB += int(card[i - 1])

    # Return True if valid, False otherwise
    return (sumA + sumB) % 10 == 0


main()
