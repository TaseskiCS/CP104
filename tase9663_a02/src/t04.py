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

num_flyers = int(input("Number of flyers: "))
num_delivery_people = int(input("Number of delivery people: "))

# num of flyers each delivery person receives
flyers_per_person = num_flyers // num_delivery_people

# num of flyers left over
flyers_left_over = num_flyers % num_delivery_people

# outputs
print(f"Flyers per delivery person: {flyers_per_person}")
print(f"Flyers left over: {flyers_left_over}")
