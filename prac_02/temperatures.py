def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9


def main():
    print("The temperature Converter")

    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius:.2f}°C is {fahrenheit:.2f}°F")

    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit:.2f}°F is {celsius:.2f}°C")


if __name__ == "__main__":
    main()
