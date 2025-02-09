import random

# Main function
def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(get_score_result(random_score))

# Function that determines the result based on the score
def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

# Call
main()