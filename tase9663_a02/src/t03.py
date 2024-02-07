"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-10-18"
-------------------------------------------------------
"""
# Imports

# Constants

date_input = int(input("Enter a date in the format YYYYMMDD: "))


# 19621025
year = date_input // 10000
remaining = date_input % 10000
month = remaining // 100
day = remaining % 100

# outputs
print(f"The reformatted date: {year}/{month:02}/{day:02}")
