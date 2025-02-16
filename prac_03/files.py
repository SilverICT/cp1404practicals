# 1. Write name to name.txt

name = input("Enter your name: ")
out_file = open("name.txt", "w")  # Open for writing (creates or overwrites)
print(name, file=out_file)  # Write the name to the file
out_file.close()  # Close the file


# 2. Read name from name.txt and print greeting

in_file = open("name.txt", "r")  # Open for reading
name = in_file.read()  # Read the entire file content (which is just the name)
in_file.close()  # Close the file
print(f"Hi {name.strip()}!")  # Print the greeting, removing any leading/trailing whitespace


# 3. Read first two numbers from numbers.txt and sum them
# Create numbers.txt if it doesn't exist, and write the numbers to it.
try:
    with open("numbers.txt", "r") as in_file:  #Try to open it.
      pass #If it opens, do nothing
except FileNotFoundError:
  with open("numbers.txt", 'w') as out_file:
    out_file.write("17\n")
    out_file.write("42\n")
    out_file.write("400\n")



with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())  # Read the first line and convert to integer
    second_number = int(in_file.readline())  # Read the second line and convert to integer
    total = first_number + second_number
    print(total)


# 4. Read all numbers from numbers.txt and sum them

total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:  # Iterate through each line in the file
        number = int(line)  # Convert the line to an integer
        total += number  # Add the number to the total
    print(total)