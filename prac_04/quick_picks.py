"""
CP1404/CP5632 Practical
Quick picks

"""

import random

# Set Constants
MIN_NUM = 1
MAX_NUM = 45
NUM_PICK = 6


def generate_quick_pick():
    """Generates a line of 6 unique random numbers between 1 and 45."""
    # Set for singularity
    numbers = set()
    while len(numbers) < NUM_PICK:
        number = random.randint(MIN_NUM, MAX_NUM)
        numbers.add(number)

    return sorted(numbers)


def main():
    """Asks for the number of quick picks and prints them."""
    # Ask the user how many quick picks they want
    num_picks = int(input("How many quick picks? "))

    # Generate and print the quick picks
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        # Print each quick pick with formatting for neat alignment
        print(" ".join(f"{num:2}" for num in quick_pick))


main()