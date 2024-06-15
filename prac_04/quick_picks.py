import random

min_number = 1
max_number = 45
num_per_pick = 6


def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < num_per_pick:
        number = random.randint(min_number, max_number)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


if __name__ == "__main__":
    main()
