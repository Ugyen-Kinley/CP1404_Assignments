"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   A ValueError will occur if the user inputs something that cannot be converted to an integer, like
    a string or a floating-point number.
2. When will a ZeroDivisionError occur?
   A ZeroDivisionError will occur if the user inputs 0 as the denominator,
   as the division by zero is undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes, it can be changed to check if the denominator is zero before attempting the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero! Please enter a valid denominator.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
