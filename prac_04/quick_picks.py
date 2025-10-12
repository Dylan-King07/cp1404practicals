import random

NUMBERS_PER_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Choose number of quick picks and print them"""
    number_of_picks = int(input("How many quick picks? "))
    for i in range(number_of_picks):
        quick_pick = generate_quick_pick()
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a quick pick with random numbers"""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return numbers


main()
