import csv
import sys
from collections import Counter


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(0)

    # TODO: Read database file into a variable
    with open(sys.argv[1], "r") as f:
        reader = csv.DictReader(f)
        db_list = list(reader)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as f:
        seq_list = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    match = {}

    for i in db_list[0]:
        match[i] = (longest_match(seq_list, i))

    # TODO: Check database for matching profiles
    # Declare an empty list of matches
    max = len(match) - 1
    coincidences = 0
    found = "No match"

    # Cycle through all the people and all the STR
    for i in range(len(db_list)):
        for j in match:
            # If a person's STR == STR, there's match
            if str(match[j]) == db_list[i][j]:
                # We increase coincidences by 1
                coincidences += 1
                if coincidences == max:
                    found = db_list[i]["name"]

        coincidences = 0
    # Print the found match
    print(found)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
