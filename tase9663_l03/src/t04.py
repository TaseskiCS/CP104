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

num = float(input('Enter number: '))
percent = float(input('Enter percent: '))
discount = num * (percent/100)
print(f'A {percent} percent discount on {num} is {discount:.1f}')
