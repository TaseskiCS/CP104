"""
-------------------------------------------------------
[Ingredients Calculator For Mac & Cheese Servings]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-29"
-------------------------------------------------------
"""
# Constants
MILK_CUPS = 4
BUTTER_TBSP = 8
FLOUR_CUPS = 0.5
SALT_TSP = 2

# Take input for servings of mac and cheese
serving_inp = int(input("Enter servings of Mac & Cheese: "))

# TODO: calculations for each amount, each are divided by 6 because that represents 1 serving.
milk_amt = float(MILK_CUPS / 6 * serving_inp)
butter_amt = float(BUTTER_TBSP/6 * serving_inp)
flour_amt = float(FLOUR_CUPS/6 * serving_inp)
salt_amt = float(SALT_TSP/6 * serving_inp)

# Outputs
print(f'{serving_inp} servings of Mac & Cheese requires: ')
print(f'milk (cups): {milk_amt}')
print(f'butter (tablespoons): {butter_amt}')
print(f'flour (cups): {flour_amt}')
print(f'salt (teaspoons): {salt_amt}')
