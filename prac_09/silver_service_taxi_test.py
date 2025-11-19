from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main function to test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)
    taxi.start_fare()
    taxi.drive(18)
    expected_fare = 48.78
    actual_fare = taxi.get_fare()
    test_result = f"Expected fare: {expected_fare}, got {actual_fare}"

    # Fail test
    assert abs(actual_fare - expected_fare) < 0.01, test_result

    print(test_result)


main()
