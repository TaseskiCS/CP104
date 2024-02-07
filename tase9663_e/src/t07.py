"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Antonio Taseski
ID:     169069663
Email:  tase9663@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from t07_functions import line_lengths
# your imports here

# Your code here
f_in = open('source.txt', 'r', encoding='utf-8')
f_short = open('f_short.txt', 'w')
f_long = open('f_long.txt', 'w')

n = int(input('Enter the length amount of lines: '))


print(line_lengths(f_in, f_short, f_long, n))

f_in.close()
f_short.close()
f_long.close()
