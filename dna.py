import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # TODO: Read database file into a variable
    titles = []
    people = []
    with open(sys.argv[1], "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(len(row)):
                titles.append(row[i])
            break

        for row in reader:
            person = {}
            for i in range(len(titles)):
                person[titles[i]] = row[i]
            people.append(person)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file:
        sequence = file.read().strip()

    # TODO: Find longest match of each STR in DNA sequence
    match = {}
    for i in range(1, len(titles)):
        match[titles[i]] = longest_match(sequence, titles[i])

    # TODO: Check database for matching profiles
    for i in range(len(people)):
        counter = 0
        for j in range(1, len(titles)):
            if int(people[i][titles[j]]) == match[titles[j]]:
                counter += 1
        if counter == len(titles) - 1:
            print(people[i][titles[0]])
            sys.exit(0)

    print("No match")
    sys.exit(1)


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
