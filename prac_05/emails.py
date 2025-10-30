"""
Emails
Estimated time: 40 minutes
Actual time: 1 hour
"""


def main():
    """Dictionary of emails and names"""
    email_to_name = {}
    input_email = input("Email: ")
    while input_email != "":
        suggested_name = get_email_name(input_email)
        name_confirmation = input(f"Is your name {suggested_name}? (Y/n)")

        if name_confirmation.upper() != "Y" and name_confirmation != "":
            actual_name = input("Name: ")
        else:
            actual_name = suggested_name

        email_to_name[input_email] = actual_name
        input_email = input("Email: ")

    for input_email, actual_name in email_to_name.items():
        print(f"{actual_name} ({input_email})")


def get_email_name(input_email):
    """From the email address, extract the name"""
    split_name_from_email = input_email.split('@')[0]
    split_prefixes = split_name_from_email.split('.')
    actual_name = " ".join(split_prefixes).title()
    return actual_name


main()
