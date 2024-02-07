"""
-------------------------------------------------------
[Monthly Payment For Mortgage]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-19"
-------------------------------------------------------
"""
# Imports


# User input for mortgage principal amount
mortgage_principal = float(input("Mortgage principal ($): "))  # p

# User input for number of years mortgage runs
num_of_years = int(input("Number of years: "))

# User input for yearly interest rate
yearly_interest_rate = float(input("Yearly interest rate (%): "))

# Takes the 5% or 5.0 and converts to 0.05
yearly_percentage = (yearly_interest_rate / 100)
# Constants
monthly_interest_payments = yearly_percentage / 12  # i

num_of_monthly_payments = num_of_years * 12  # n


# TODO: Calculation for monthly payment

numerator = mortgage_principal * \
    (monthly_interest_payments * (1 + monthly_interest_payments)**num_of_monthly_payments)

denominator = ((1 + monthly_interest_payments) ** num_of_monthly_payments) - 1

monthly_payment = numerator / denominator

# Outputs
print(f"The monthly payments are: $ {monthly_payment}")
