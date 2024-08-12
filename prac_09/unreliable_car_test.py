from prac_09.unreliable_car import UnreliableCar


def main():
    # Create a new UnreliableCar object with name "Junk Car", 100 units of fuel, and 50% reliability
    my_unreliable_car = UnreliableCar("Junk Car", 100, 50)

    # Try to drive the car 40 km
    distance_driven = my_unreliable_car.drive(40)
    print(f"Distance driven: {distance_driven} km")

    # Print the car's details
    print(my_unreliable_car)


if __name__ == "__main__":
    main()
