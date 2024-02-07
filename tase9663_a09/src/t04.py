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
from functions import line_numbering
# Constants

fh = open("wilde.txt", "r+", encoding="utf-8")

line_numbering(fh, fh)
