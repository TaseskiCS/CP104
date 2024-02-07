"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports
from functions import magic_date
# Constants
day = int(input('Enter Day: '))
month = int(input('Enter Month: '))
year = int(input('Enter Year: '))

magic = magic_date(day, month, year)

print(magic)
