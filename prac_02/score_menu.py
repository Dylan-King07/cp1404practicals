# def print_line(length):
#     print('-' * length)
#
# def print_grid(number_of_rows, number_of_columns):
#     #Version 1
#     # for i in range(number_of_rows):
#     #     for j in range(number_of_columns):
#     #         print('*', end="")
#     #     print()
#     #Version 2
#     # for i in range(number_of_rows):
#     #     print('*' * number_of_columns)
#     #Version 3
#     print(f"{'*' * number_of_columns}\n" * number_of_rows)
#
#
#
#
#
#
# print_grid(3, 7)
# print()
# print_grid(2, 50)

import random

def main():
    print("Menu: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            name = get_valid_name()
        elif choice == "P":
            print_greeting(name)
        elif choice == "S":
            print_secret_name(name)
        else:
            print("Invalid Choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("Farewell")
def print_greeting():
    i = len(name)
    print_line(i)
    print(name)
    print_line(i)

def get_valid_name():
    name = input("Name: ")
    while name == "":
        print("Invalid name")
        name = input("Name: ")
    return name

def print_line(length):
     print('-' * length)

def print_secret_name(name):
    letters = list(name)
    random.shuffle(letters)
    print("".join(letters))


main()