from prac_09.unreliable_car import UnreliableCar

TEST_RUNS = 100
TEST_DISTANCE = 30


def main():
    """Function to test Car Reliability."""
    cars = {
        "Working (100%)": UnreliableCar("Working", 10000000, 100),
        "Reliable (85%)": UnreliableCar("Reliable", 10000000, 85),
        "Unreliable (30%)": UnreliableCar("Unreliable", 10000000, 30),
        "Broken (0%)": UnreliableCar("Broken", 10000000, 0)
    }

    success_count = {name: 0 for name in cars}

    print(f"Over {TEST_RUNS} test runs:")
    for index in range(TEST_RUNS):
        for name, car in cars.items():
            if car.drive(TEST_DISTANCE) > 0:
                success_count[name] += 1

    for name, count in success_count.items():
        print(f"{name}: Drove {count} times")


main()
