MIN_LENGTH = 7

def main():
    # Get a valid password
    password = get_password(MIN_LENGTH)

    # Print asterisks for the length
    print_asterisks(password)

def get_password(min_length):
    # Input the password
    password = input("Enter a password: ")

    # Keep asking if the password is less than the minimum
    while len(password) < min_length:
        print(f"Password must have at least {min_length} characters.")
        password = input("Enter a password: ")

    return password


def print_asterisks(password):
    # Print asterisks based on the length
    print('*' * len(password))


# Call
main()