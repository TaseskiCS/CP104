"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-29"
-------------------------------------------------------
"""
# Imports

# Constants
WIDTH = 7
DECIMAL_PLACE = 2
breakfast_cost = float(input("Enter cost of breakfast: $"))
lunch_cost = float(input("Enter cost of lunch: $"))
supper_cost = float(input("Enter cost of supper: $"))

# Calculate the total cost
total_cost = breakfast_cost + lunch_cost + supper_cost

# Display the formatted table
print(f"Meal         Cost")
print(f"Breakfast    $ {breakfast_cost:7.2f}")
print(f"Lunch        $ {lunch_cost:7.2f}")
print(f"Supper       $ {supper_cost:7.2f}")
print(f"Total        $ {total_cost:7.2f}")
