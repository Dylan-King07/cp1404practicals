"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Adds line which exits the loop if a valid integer is inputted
    except ValueError:  # Checks for a ValueError and tells user to enter a valid integer
        print("Please enter a valid integer.")
print("Valid result is:", result)
