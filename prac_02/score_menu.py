def main():
    score = get_valid_score() # Gets initial score so that all menu options can be chosen first
    menu = """Menu options:
    G = Get valid score
    P = Print result
    S = Show stars
    Q = Quit program"""
    print(menu)
    choice = input("Choose menu option: ").upper()
    print(choice)
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_status(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid Choice")
        print(menu)
        choice = input("Choose menu option: ").upper()
    print("Farewell")


def get_valid_score():
    score = float(input("Enter score between 0 and 100: ")) #This requires the user to input a number, if the user inputs a string, the program will error
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score between 0 and 100: "))
    return score


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