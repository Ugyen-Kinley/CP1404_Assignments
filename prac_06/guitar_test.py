from guitar import Guitar


def test_guitar_methods():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 500.0)

    current_year = 2022
    expected_gibson_age = 100
    expected_another_guitar_age = 9
    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson.get_age(current_year)}")
    print(
        f"{another_guitar.name} get_age() - Expected {expected_another_guitar_age}. Got {another_guitar.get_age(current_year)}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(current_year)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(current_year)}")


if __name__ == "__main__":
    test_guitar_methods()
