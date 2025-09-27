from random import randint
low_number = int(input("Input low number: "))
high_number = int(input("Input high number: "))
while high_number <= low_number:
    print("High number must be larger than low number")
    low_number = int(input("Input low number: "))
    high_number = int(input("Input high number: "))
number_of_smilies = randint(low_number, high_number)
print(":) " * number_of_smilies)
