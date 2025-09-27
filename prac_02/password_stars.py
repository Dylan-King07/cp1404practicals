# Main function
def main():
    password = get_password()
    print_password_asterisks(password)

def get_password() -> str:
    minimum_length = int(input("Enter minimum character limit: "))
    password = input(f"Input password with at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Input password with at least {minimum_length} characters: ")
    return password

def print_password_asterisks(password: str):
    print(f"Password: {'*' * len(password)}")

main()