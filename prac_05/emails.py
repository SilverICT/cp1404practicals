"""
emails
Estimate: 20 minutes
Actual:   23 minutes


"""


def main():
    """Main function to collect emails and names, and display them."""
    email_to_name = {}
    email = input("Email: ")


    while email != "":
        try:
            name = extract_name_from_email(email)
        except ValueError as e:
            print(f"Error: {e}")
            email = input("Email: ")
            continue

        confirmation = input(f"Is your name {name}? (Y/N) ").lower()

        if confirmation != 'y' and confirmation != '':
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email(Press enter to finish): ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract a name from an email address."""
    if '@' not in email:
        raise ValueError("Invalid email format. Missing '@' symbol.")

    # Get the part before the '@'
    local_part = email.split('@')[0]

    # Split the local part by non-alphabet characters
    name_parts = ''.join(char if char.isalpha() else ' ' for char in local_part).split()

    if not name_parts:
        raise ValueError("Cannot extract name from email.")

    # Convert to title case
    name = " ".join(name_parts).title()
    return name



main()