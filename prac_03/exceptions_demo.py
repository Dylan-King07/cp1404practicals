"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:                                    # Checks denominator until non-zero integer entered
        print("Cannot divide by zero")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


"""
1. When will a ValueError occur?
"""
# A ValueError will occur when a letter, such as a, a float, such as 3.9 or symbol such as $ or # is entered.


"""
2. When will a ZeroDivisionError occur?
"""
# A ZeroDivisionError will occur when a 0 is entered for the denominator value.


"""
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
# You can avoid a ZeroDivisionError.
# This can be done by adding a while loop to reprompt the denominator until a non-zero integer is entered.

