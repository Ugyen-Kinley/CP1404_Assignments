"""
Hexadecimal Colour Codes Lookup
Estimate: 15 minutes
Actual:   18 minutes
"""

colour_to_hex = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


def main():
    print("The Colour Codes Lookup")
    colour_name = input("Enter the colour name: ").strip().lower()
    while colour_name != "":
        try:
            hex_code = colour_to_hex[convert_to_camel_case(colour_name)]
            print(f"{colour_name} is {hex_code}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").strip().lower()


def convert_to_camel_case(name):
    return ''.join(word.capitalize() for word in name.split())


if __name__ == "__main__":
    main()
