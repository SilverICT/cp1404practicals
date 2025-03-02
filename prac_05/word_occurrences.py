"""
Word Occurrences
Estimate: 10 minutes
Actual:   16 minutes

Work done:
Create dictionary to store word
Fplit strings into words and count it
Find the longest word length for formatting
Sorted by length
Loop the program and give it an end
"""



def count_word_occurrences(text):
    # Create a dictionary to store word counts
    word_counts = {}

    # Split the string into words
    words = text.split()

    # Count the occurrences of each word
    for word in words:
        # .lower for case-insensitive
        word = word.lower()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    #
    max_word_length = max(len(word) for word in word_counts)

    # Sort the dictionary by key (word)
    sorted_words = sorted(word_counts.items())

    # Print the sorted words and their counts, aligned
    for word, count in sorted_words:
        print(f"{word:{max_word_length}} : {count}")


def main():
    text = input("Enter a string of text: ")
    count_word_occurrences(text)

    # Continue asking for input until the user enters a blank string
    while text != "":
        # Call the function to count word occurrences
        count_word_occurrences(text)

        # Ask for new input
        text = input("Enter a string of text (or press Enter to quit): ")

    print("See u next time")


main()