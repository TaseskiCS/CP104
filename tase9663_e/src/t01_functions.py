"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Antonio Taseski
ID:     169069663
Email:  tase9663@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌‌​​‌‌​​​‌​‌‌‌‌‌:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """
    total = 0
    count = 0
    ea = 0
    for i in range(len(values)):
        if values[i] % 2 == 0:
            total += values[i]
            count += 1
        if count == 0:
            ea = 0
        else:
            ea = total // count

    # your code here

    return ea
