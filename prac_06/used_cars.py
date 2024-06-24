from prac_06.car import Car


def main():
    my_car = Car(name="My Car", fuel=180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    Honda = Car(name="Honda", fuel=100)
    Honda.add_fuel(20)
    print(f"Fuel in the Honda: {Honda.fuel}")
    distance_driven = Honda.drive(115)
    print(f"Distance driven: {distance_driven}")
    print(Honda)


main()
