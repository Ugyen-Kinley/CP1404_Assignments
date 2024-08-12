import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car with unreliable driving capability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on reliability."""
        # Generate a random number between 0 and 100
        chance = random.uniform(0, 100)

        if chance < self.reliability:
            # If the chance is less than reliability, drive the car
            distance_driven = super().drive(distance)
        else:
            # Otherwise, do not drive and set distance_driven to 0
            distance_driven = 0

        return distance_driven

    def __str__(self):
        """Return a string representation of an UnreliableCar object."""
        return f"{super().__str__()}, reliability={self.reliability}%"
