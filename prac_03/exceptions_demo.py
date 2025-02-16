"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when input is not integer
2. When will a ZeroDivisionError occur?
when denominator input as 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, check if the input is 0 at denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:   #check if the input is 0 at denominator
        print("Denominator cannot be zero. Please enter a non-zero value.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")