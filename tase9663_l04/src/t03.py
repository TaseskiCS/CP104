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
from functions import area
# Constants

radius = float(input('Enter a radius: '))

circle_area = area(radius)
# output
print(f'{circle_area:.2f}')
