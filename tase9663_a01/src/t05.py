"""
-------------------------------------------------------
[Compound Interest]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""
# Take user input for principal, interest percentage, number of years, and annual compound
principal = float(input('Principal: $'))
interest_percentage = float(input('Interest (%): '))
num_years = int(input('Number of years: '))
num_annual_compound = int(
    input('Number of times interest compounded per year: '))

# Divide interest_percentage by 100 to turn it into 0.05 given input 5.0
interest_rate = interest_percentage / 100
expo = num_annual_compound * num_years

# Plug in each value into compound interest formula
balance = principal * (1 + (interest_rate/num_annual_compound))**expo

# Outputs
print(f'Balance: $ {balance}')
