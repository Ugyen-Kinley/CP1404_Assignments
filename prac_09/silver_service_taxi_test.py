from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi with fanciness of 2
    fancy_taxi = SilverServiceTaxi("Lux Taxi", 100, 2)

    # Start a fare and drive 18 km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Calculate expected fare
    expected_fare = (2 * 1.23 * 18) + SilverServiceTaxi.flagfall
    actual_fare = fancy_taxi.get_fare()

    # Print the taxi's details and fare
    print(fancy_taxi)
    print(f"Fare for the trip: ${actual_fare:.2f}")

    # Assert that the actual fare matches the expected fare
    assert abs(actual_fare - expected_fare) < 0.01, f"Expected fare: ${expected_fare}, but got: ${actual_fare}"

if __name__ == "__main__":
    main()
