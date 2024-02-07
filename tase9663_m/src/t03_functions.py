"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Antonio Taseski
ID:     169069663
Email:  tase9663@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants
BASE_COST = 125.00
COST_PER_SERVICE = 25.00
DISCOUNT = 0.1
# your constants here


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​​‌‌​​​‌​‌‌‌‌‌:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    services = float(input('How many extra services are you purchasing? '))
    vip = str(input('Are you a VIP member (Y/N)? '))
    cost = BASE_COST + (COST_PER_SERVICE * services)
    if services > 1:
        if vip == 'Y':
            discounted_cost = DISCOUNT * cost
            cost = cost - discounted_cost

    return cost
