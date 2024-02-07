"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
from functions import print_matrix_num, generate_matrix_num
# Constants

matrix = generate_matrix_num(3, 4, -10, 10, "float")

print_matrix_num(matrix, 'float')
