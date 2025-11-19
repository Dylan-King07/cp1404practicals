from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent a car which is unreliable and sometimes does not work."""

    def __init__(self, name, fuel, reliability):
        """Initialise properties of UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if random generated number falls below the reliability percentage."""
        random_number = randint(1, 100)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return 0

