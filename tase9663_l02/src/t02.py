"""
-------------------------------------------------------
[Temperature Converter]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-19"
-------------------------------------------------------
"""
# Imports

# Constants

# TODO: Define Water Freezing Point
FREEZING = 32


# Receive users input in Fahrenheit, take as int to be able to do arithmitic on it
fahrenheit = int(input("Temperature(F): "))

# TODO: Calculate New Temperature in Celsius
celsius = (fahrenheit - FREEZING) * 5/9  # Fahrenheit to Celsius formula

# Outputs
print("Temperature(C): ", celsius)
