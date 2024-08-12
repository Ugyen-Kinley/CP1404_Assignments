from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def display_taxis(taxis):
    """Display the list of available taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Allow the user to choose a taxi from the list."""
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    """Drive the selected taxi for a given distance and return the cost."""
    try:
        distance = float(input("Drive how far? "))
        cost = taxi.drive(distance)
        print(f"Your {taxi.name} trip cost you ${cost:.2f}")
        return cost
    except ValueError:
        print("Invalid distance")
        return 0


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    current_taxi = None
    total_bill = 0

    while True:
        print("\nLet's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        option = input(">>> ").strip().lower()

        if option == 'q':
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif option == 'c':
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
            if current_taxi is None:
                print(f"Bill to date: ${total_bill:.2f}")
        elif option == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                cost = drive_taxi(current_taxi)
                total_bill += cost
                print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")


if __name__ == '__main__':
    main()
