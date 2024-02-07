"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""
# Imports

CONVERSION_FACTOR = 1.61  # Miles to km multiple
# Constants

miles = float(input('Length in miles: '))

km = miles * CONVERSION_FACTOR  # Conversion

# Output
print(f'Length in km: {km}')
