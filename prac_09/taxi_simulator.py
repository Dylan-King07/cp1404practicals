"""
CP1404 Prac_09, Taxi Simulator Exercise
Estimated time: 1 hour
Actual time:
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "(q)uit, (c)hoose taxi, (d)rive"


def main():
    """Main function for taxi simulator program which utilises Taxi and SilverServiceTaxi classes."""
    print("Let's drive!")
    print(MENU)

    taxis = initialise_taxis()
    current_taxi = None
    total_bill = 0

    choose_option = get_menu_choice()
    while choose_option != "q":
        if choose_option == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choose_option == "d":
            trip_cost = drive_taxi(current_taxi)
            total_bill += trip_cost
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


def choose_taxi(taxis):
    """Input a taxi and return it."""
    try:
        taxi_number = int(input("Choose taxi: "))
        return taxis[taxi_number]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def drive_taxi(current_taxi):
    """Ensure a taxi is selected and prompt user for a driving distance."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive.")
        return 0.0
    current_taxi.start_fare()

    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0
    current_taxi.drive(distance)
    cost = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
    return cost


if __name__ == "__main__":
    main()
