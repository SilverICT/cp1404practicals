"""
CP1404/CP5632 Practical
In the starter code, it had initialize an empty list to store the monthly incomes;
It gets the users' input for the number of month;
It used for loop to convert the monthly income input into float and append the value to the income list
It had calculate the total at the end.

work done:
1.Uses f-string instead of string concatenation.
2.Refactor the months variable to a better name , num_months
3.Refactor the report printing to a function
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        #uses an f-string instead of string concatenation (+).
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    #Call the function
    print_report(incomes, num_months)


#Put it into function
def print_report(incomes, num_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, num_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()


