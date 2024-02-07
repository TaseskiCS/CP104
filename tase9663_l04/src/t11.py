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
from functions import slope
# Constants
x1 = float(input('Pick a first x point: '))
x2 = float(input('Pick a second x point: '))
y1 = float(input('Pick a first y point: '))
y2 = float(input('Pick a second y point: '))

m = slope(x1, x2, y1, y2)
# output
print(f'{m:.1f}')
