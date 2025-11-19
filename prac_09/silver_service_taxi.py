from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Taxi with properties such as a fanciness multiplier and a flagfall cost."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi properties."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Calculate total fare."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """String describing SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
