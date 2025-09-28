"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score between 0 and 100: "))
    result = get_score_status(score)
    print(result)

    #Random score generator
    random_score = random.uniform(0, 100)
    print(f"\nRandom score: {random_score:.2f}")
    print(get_score_status(random_score))

def get_score_status(score: float):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
