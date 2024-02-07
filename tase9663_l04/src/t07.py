"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports
from functions import total_change
# Constants


nickels = int(input('Amount of nickels: '))
dimes = int(input('Amount of dimes: '))
quarters = int(input('Amount of nickels: '))
loonies = int(input('Amount of nickels: '))
toonies = int(input('Amount of nickels: '))

total = total_change(nickels, dimes, quarters, loonies, toonies)
# Output
print(total)
