from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi with added features for premium service."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel, Taxi.price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """Return a string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"
