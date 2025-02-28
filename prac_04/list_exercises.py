"""CP1404/CP5632 Practical
Basic list operations
"""

def main():
    """Main function that calls the appropriate functions."""
    # Get 5 numbers from the user and store them
    numbers = get_numbers()

    # Display statistics about the numbers
    display_statistics(numbers)

    # Ask for the username and check access
    user_input = input("Enter your username: ")
    check_access(user_input)


def get_numbers():
    """Prompt user for 5 numbers and store them in a list."""
    numbers = []
    for i in range(5):
        number = float(input(f"Number: "))  # Grab user input
        numbers.append(number)  # Store in list
    return numbers


def display_statistics(numbers):
    """Display statistics about the list of numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def check_access(user_input):
    """Check if the entered username is in the list of authorized users."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']

    if user_input in usernames:
        print("Access granted.")  # Username is authorized
    else:
        print("Access denied.")  # Username is not authorized


main()

