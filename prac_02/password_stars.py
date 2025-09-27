# Main function
def main():
    minimum_length = int(input("Enter minimum character limit: "))
    password = password_input(minimum_length)
    print_stars(password)

# Function for customising password
def password_input(minimum_length):
    password = input(f"Input password with at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Input password with at least {minimum_length} characters: ")
    return password

# Printing the password using asterisks
def print_stars(password):
    print(f"Password: {'*' * len(password)}")

main()