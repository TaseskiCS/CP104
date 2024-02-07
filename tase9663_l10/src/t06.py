"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-11-21"
-------------------------------------------------------
"""
# Imports
from functions import number_stats
# Constants


file = open('numbers.txt', 'r', encoding='utf-8')

smallest, largest, total, average = number_stats(file)

print('Smallest: %s' % smallest)
print('Largest: %s' % largest)
print('Total: %s' % total)
print('Average: %s' % average)
