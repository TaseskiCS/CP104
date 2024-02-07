"""
-------------------------------------------------------
Midterm B Task 1 Function Definitions
-------------------------------------------------------
Author: Antonio Taseski
ID:     169069663
Email:  tase9663@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants
LOONIES_WORTH = 100
QUARTERS_WORTH = 25
DIMES_WORTH = 10
NICKELS_WORTH = 5
# your constants here


def minimal_change(cents):
    """
    -------------------------------------------------------
    Breaks down cents into a minimal number of coins.
    The change can be:
        loonies - coins worth 100 cents
        quarters - coins worth 25 cents
        dimes - coins worth 10 cents
        nickels - coins worth 5 cents
    Use: loonies, quarters, dimes, nickels = minimal_change(cents)
    -------------------------------------------------------
    Parameters:
        cents - number of cents (int >= 0)
    Returns‌​‌​​​​‌​​‌‌‌‌​​‌‌​​​‌​‌‌‌‌‌:
        loonies - number of loonies ($1 coins) (int)
        quarters - number of quarters (25 cent coins) (int)
        dimes - number of dimes (10 cent coins) (int)
        nickels - number of nickels (5 cent coins) (int)
    -------------------------------------------------------
    """

    # your code here
    loonies = cents // LOONIES_WORTH
    cents %= LOONIES_WORTH
    quarters = cents // QUARTERS_WORTH
    cents %= QUARTERS_WORTH
    dimes = cents // DIMES_WORTH
    cents %= DIMES_WORTH
    nickels = cents // NICKELS_WORTH
    return loonies, quarters, dimes, nickels
