"""
CP1404 Prac_09, Taxi Simulator Exercise
Estimated time: 1 hour
Actual time:
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = ("(q)uit\n"
        "(c)hoose taxi\n"
        "(d)rive"
        )


def main():
    """Main function for taxi simulator program which utilises Taxi and SilverServiceTaxi classes."""
    print("Let's drive!")

    taxis = initialise_taxis()
    current_taxi = None
    total_bill = 0

    print(MENU)

    choose_option = get_menu_choice()
    while choose_option != "q":
        if choose_option == "c":
            # Choose taxi function placeholder
            pass
        elif choose_option == "d":
            # Drive function placeholder
            pass
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choose_option = get_menu_choice()

    print(f"Total trip cost: ${total_bill:.2f}")
    print(f"Taxis are now: ")
    display_taxis(taxis)


def initialise_taxis():
    """Create list of taxi objects."""
    return [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]


def get_menu_choice():
    """Prompt user to input menu choice."""
    return input(">>> ").lower()


def display_taxis(taxis):
    """Display taxi list."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


if __name__ == "__main__":
    main()
