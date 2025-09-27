username = input("Enter username: ")
menu_options = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu_options)
menu_choice = input("Select menu option-> ")
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello, {username}")
    elif menu_choice == "G":
        print(f"Goodbye, {username}")
    else:
        print("Choice is invalid")
    print(menu_options)
    menu_choice = input("Select menu option-> ")
print("Finished")
