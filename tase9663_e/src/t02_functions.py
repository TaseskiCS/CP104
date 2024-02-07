"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Antonio Taseski
ID:     169069663
Email:  tase9663@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Constants
DRY_DAY = 0
DAMP_DAY = 4
WET_DAY = 8
# Your constants here


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌‌​​‌‌​​​‌​‌‌‌‌‌:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    # your code here
    dry_days = 0
    damp_days = 0
    wet_days = 0
    avg = 0
    total = 0
    count = 0
    while True:
        rain = int(input('Rainfall mm (-1 to stop): '))
        if rain == -1:
            break
        if rain < DAMP_DAY:
            dry_days += 1
            total += rain
            count += 1
        elif DAMP_DAY <= rain <= WET_DAY:
            damp_days += 1
            total += rain
            count += 1
        else:
            wet_days += 1
            total += rain
            count += 1

    avg = total // count

    return dry_days, damp_days, wet_days, avg
