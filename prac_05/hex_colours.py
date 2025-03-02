"""
Hexadecimal Colour Code

Work done:
Store data in constant dictionary.
Entering an invalid colour name the program will loop back to ask valid input
"""

COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "Aqua": "#00ffff",
    "Blue": "#0000ff",
    "Black": "#000000",
    "Pale Silver": "#c9c0bb",
    "Russian Violet": "#32174d",
    "Silver": "#c0c0c0",
    "SkyBlue": "#87ceeb",
    "White": "#ffffff",
    "Wintergreen Dream": "#56887d",
}

#Get case-insensitive input
color_name = input("Enter a color name (or blank to quit): ").strip().title()

#While loop for bounce back invalid input
while color_name:
    try:
        print(f"The hex code for {color_name} is {COLOR_CODES[color_name]}")
    except KeyError:
        print("Invalid color name.")

    color_name = input("Enter a color name (or blank to quit): ").strip().title()