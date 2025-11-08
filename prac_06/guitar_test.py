"""
CP1404 Practical 6 Guitar testing exercise
Estimated time: 15 minutes
Actual time: 15 minutes
"""

from prac_06.guitar import Guitar

CURRENT_YEAR = 2022  # Example year specified in prac
VINTAGE_AGE = 50


def main():
    """Tests for determining guitar class"""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 0)

    # Determine expected age
    expected_gibson_age = CURRENT_YEAR - gibson.year
    expected_another_age = CURRENT_YEAR - another_guitar.year
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected {expected_another_age}. Got {another_guitar.get_age()}")

    # Determine vintage status
    expected_gibson_vintage = expected_gibson_age >= VINTAGE_AGE
    expected_another_vintage = expected_another_age >= VINTAGE_AGE
    print(f"{gibson.name} is_vintage() - Expected {expected_gibson_vintage}. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} get_age() - Expected {expected_another_vintage}. Got {another_guitar.is_vintage()}")


if __name__ == "__main__":
    main()
