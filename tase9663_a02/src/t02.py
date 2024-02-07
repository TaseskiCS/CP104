"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants

num = int(input("Enter a positive two-digit number: "))


first_digit = num // 10  # gets 2 from example 25
second_digit = num % 10  # gets 5 from example 25

# difference of the two digits
difference = first_digit - second_digit

# output
print(f"The difference of the digits of {num} is {difference}")
