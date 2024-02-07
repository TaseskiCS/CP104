"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import read_integers
# Constants


file_handle = open("numbers.txt", "r", encoding="utf-8")

print(read_integers(file_handle))

file_handle.close()
