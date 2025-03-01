"""
CP1404/CP5632 Practical - week 5
State names in a dictionary
File needs reformatting

Work done:
Reformat Code or use the keyboard shortcut (Command+option+L)
Use .strip() .upper() for case-insensitive input
Use try, except for "Easier to Ask Forgiveness than Permission" (EAFP)
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

# Print all state codes and names in aligned format
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

#Get case-Insensitive Input
state_code = input("Enter short state: ").strip().upper()

#Response on invalid input and bonce back
while state_code:
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")

    state_code = input("Enter short state: ").strip().upper()