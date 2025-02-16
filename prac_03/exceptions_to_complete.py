"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit the loop if input is valid
    except ValueError:
        (print("Please enter a valid integer.")) # Catch the ValueError specifically
print("Valid result is:", result)