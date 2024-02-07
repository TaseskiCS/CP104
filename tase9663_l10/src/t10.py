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
from functions import count_frequency_word
# Constants


word = str(input('Word to count: '))
file = open('words.txt', 'r')

count = count_frequency_word(file, word)

print('%s appeared %d time(s)' % (word, count))
