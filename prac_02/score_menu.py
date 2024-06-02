import random


def main():
    score = get_valid_score()
    choice = ''
    while choice != 'Q':
        display_menu()
        choice = input("Choose an option: ").upper()
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = determine_result(score)
            print(f"Your result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice. Please try again.")


def display_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    score = float(input("Enter your score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter your score (0-100): "))
    return score


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print('*' * int(score))


if __name__ == "__main__":
    main()
