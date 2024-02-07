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
from functions import customer_record
# Constants

file = open('customers.txt', 'r', encoding='utf-8')

record = int(input('Find a record n\nEnter a record number: '))

print(customer_record(file, record))
