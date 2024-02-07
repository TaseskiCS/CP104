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
COMPANY_TAX_RATE = 18.5 / 100  # 18.5%

total_sales = float(input("Enter the total sales: $"))

# calculate the annual tax
annual_tax = total_sales * COMPANY_TAX_RATE

# outputs
print("Projected Tax Report")
print("--------------------------")
print(f"Total sales:   $ {total_sales:.2f}")
print(f"Annual tax:    % {COMPANY_TAX_RATE * 100:.2f}")
print("--------------------------")
print(f"Tax:           $ {annual_tax:.2f}")
