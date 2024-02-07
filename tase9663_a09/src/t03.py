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
from functions import file_statistics
# Constants


file_handle = open("addresses.txt", "r", encoding="utf-8")

print(file_statistics(file_handle))

file_handle.close()
