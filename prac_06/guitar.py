"""
CP1404 Practical 6 Guitars! exercise
Estimated time: 10 minutes
Actual time: 12 minutes
"""


CURRENT_YEAR = 2022  # Example year specified in prac
VINTAGE_AGE = 50


class Guitar:
    """Guitar with details of the name, year of creation and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise guitar information.

        name: string, guitar names
        year: integer, year of guitar creation
        cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the guitar information as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the car is older than 50 years and can be considered vintage."""
        return self.get_age() >= VINTAGE_AGE
