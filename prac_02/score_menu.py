# Main function
def main():
    print("Score Menu")

    # Get a valid score before entering the menu loop
    score = get_valid_score()

    menu = """
    (G)et a valid score
    (P)rint result
    (S)how stars
    (Q)uit
    """

    choice = input(f"{menu}>>> ").upper()

    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = get_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            print_stars(score)
        else:
            print("Invalid option, please try again.")

        choice = input(f"{menu}>>> ").upper()

    print("Farewell!")


# Function to get a valid score (only numeric input)
def get_valid_score():
    score = input("Enter score: ")

    # Check for valid numeric input and within range
    if score.isdigit():
        score_float = float(score)
        if 0 <= score_float <= 100:
            return score_float
        else:
            print("Score must be between 0 and 100. Please try again.")
            return get_valid_score()  # ask again if the score is invalid
    else:
        print("Invalid input. Please enter a valid numeric score.")
        return get_valid_score()  #ask again if the input is not numeric


# Function to determine the result based on score
def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


# Function to print stars based on score
def print_stars(score):
    print('*' * int(score))  # Print stars based on the score


# Call
main()