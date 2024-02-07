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
from functions import pythag
# Constants


side1 = float(input('Enter size of side 1: '))
side2 = float(input('Enter size of side 2: '))

r, d, c, a = pythag(side1, side2)
# output
print(f'({r:.1f}, {d:.1f}, {c}, {a})')
