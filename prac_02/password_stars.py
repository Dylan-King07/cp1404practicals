# Main function
def main():
    minimum_length = int(input("Enter minimum character limit: "))
    password = input(f"Input password with at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Input password with at least {minimum_length} characters: ")
    print(f"Password: {'*' * len(password)}")
    return password

main()