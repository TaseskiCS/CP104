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
from functions import f_to_c
# Constants

fahr_temp = float(input('Temperature in fahrenheit: '))

cels_temp = f_to_c(fahr_temp)

# Output
print(f'{cels_temp:.0f}')
