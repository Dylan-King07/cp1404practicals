from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main function to test SilverServiceTaxi."""
    taxis = {
        "Normal Taxi (x1)": SilverServiceTaxi("Normal", 100, 1),
        "Good Taxi (x2)": SilverServiceTaxi("Good", 100, 2),
        "Fancy Taxi (x3)": SilverServiceTaxi("Fancy", 100, 3)
    }

    for label, taxi in taxis.items():
        print(f"Testing {label}")
        taxi.start_fare()
        taxi.drive(18)
        fare = taxi.get_fare()
        print(f"Taxi details: {taxi}")
        print(f"Fare: ${fare:.2f}")


main()
