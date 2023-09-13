# TODO
from cs50 import get_string
import re
# Define the main function


def main():
    # Grab the text
    text = get_string("Text: ")

    # Call the function
    result = coleman(text)

    # Test the results
    if result < 1:
        print("Before Grade 1")
    elif result > 16:
        print("Grade 16+")
    else:
        print(f"Grade {result}")
# Create the function to calculate


def coleman(text):
    # Identiy the values
    characters, words, sentences = 0, 1, 0
    # Start the loop
    for i in text:
        if i in [".", "!", "?"]:
            sentences += 1
        elif i == " ":
            words += 1
        elif i.isalpha():
            characters += 1

    # Define the values for the formula
    l = 100 * (characters / words)
    s = 100 * (sentences / words)

    # Complete the formula
    result = (0.0588 * l) - (0.296 * s) - 15.8

    # Retrieve the value
    return round(result)


main()
