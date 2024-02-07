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
from functions import file_copy
# Constants


read = open('words.txt', 'r')
write = open('new_words.txt', 'w')

file_copy(read, write)

print("Copying 'words.txt' to 'new_words.txt'")
