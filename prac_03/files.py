# 1
name = input("Enter name: ")  # Prompt user for a file name
out_file = open("name.txt", "w")  # Open file
print(name, file=out_file)  # Print contents to file
out_file.close()  # Close file


# 2
in_file = open("name.txt", 'r')  # Open file in read mode
name = in_file.read().strip()  # Retrieve name from file
in_file.close()  # Close file
print(f"Hi {name}!")  # Print name from the file


# 3
with open("numbers.txt", "r") as in_file:
    number_one = int(in_file.readline())  # Read first line of file
    number_two = int(in_file.readline())  # Read second line of file
    print(number_one + number_two)  # Print sum of both numbers


# 4
total = 0  # Set total value to 0
with open("numbers.txt", "r"):  # Open numbers.txt file in read mode
    for line in in_file:  # Loop through the file line by line
        total += int(line)  # Convert string into integer
print(total)  # Print the total
