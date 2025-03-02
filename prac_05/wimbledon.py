"""
wimbledon
Estimate: 30 minutes
Actual:   48 minutes
"""


def read_data(filename):
    """Read the data from the file and return a list of lists representing each line."""
    champions_data = []

    # Open the file with the correct encoding to handle the BOM
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            # Skip the header line
            if not line.startswith("Year"):
                columns = line.strip().split(",")
                champions_data.append(columns)

    return champions_data


def count_champions(champions_data):
    """Count the number of times each champion has won and return a dictionary."""
    champions_count = {}

    # Iterate through the data to count the champions
    for row in champions_data:
        champion = row[2]  # Champion's name is in the 3rd column
        if champion in champions_count:
            champions_count[champion] += 1
        else:
            champions_count[champion] = 1

    return champions_count


def get_countries(champions_data):
    """Get the set of countries that have won Wimbledon."""
    countries = set()

    # Add the country of each champion to the set
    for row in champions_data:
        country = row[1]  # Country of the champion is in the 2nd column
        countries.add(country)

    return countries


def main():
    """Main function to run the program."""
    filename = "wimbledon.csv"

    # Step 1: Read the data from the file
    champions_data = read_data(filename)

    # Step 2: Count the champions and their wins
    champions_count = count_champions(champions_data)

    # Step 3: Get the set of countries that have won
    countries = get_countries(champions_data)

    # Step 4: Print the champions and the number of wins
    print("Wimbledon Champions: ")
    for champion, count in sorted(champions_count.items()):
        print(f"{champion} {count}")

    # Step 5: Print the countries in alphabetical order
    print("\nThese countries have won Wimbledon: ")
    sorted_countries = sorted(countries)
    print(", ".join(sorted_countries))


main()
