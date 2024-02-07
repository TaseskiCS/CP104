"""
-------------------------------------------------------
[Work Pay Calculator]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-19"
-------------------------------------------------------
"""

# Receive user input for hourly pay
hourly_wage = float(input("Hourly rate of pay: $"))

# Receive user input for hours worked in week
hours_worked_in_week = float(input("Hours worked in the week: "))

total_pay = hourly_wage * hours_worked_in_week

print(f'Total pay for the week: ${total_pay}')
