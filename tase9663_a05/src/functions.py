"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants

# t01


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """

    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


# print(calc_factorial(7))

# t02
def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes.
    Use: calories_treadmill(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (float)
        minutes - total number of minutes run (int)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(5, minutes + 1, 5):
        calories = per_min * i
        print(f"{i:3} {calories:.1f}")

    return None


#calories_treadmill(4.1, 5)
# t03


def arrow_up(n):
    """
    -------------------------------------------------------
    Prints arrow pointing up
    Use: output = arrow_up(n)
    -------------------------------------------------------
    Parameters:
        n - height of arrow (int)
    Returns:
        None 
    ------------------------------------------------------
    """
    for i in range(n):
        if i == 0:
            print(" " * (n - i - 1) + "#")
        elif i == n - 1:
            print("#" + " " * (2 * i - 1) + "#")
        else:
            print(" " * (n - i - 1) + "#" + " " * (2 * i - 1) + "#")
    return None

# t04


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print(" " * 7, end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:5}", end="")
    print("\n" + " " * 7 + "-" * 17)
    for i in range(start_num, stop_num + 1):
        print(f"{i:2} |", end="")
        for j in range(start_num, stop_num + 1):
            print(f"{i * j:6}", end="")
        print()
    return None


#multiplication_table(2, 4)


# t05

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, count+1, increment):
        total = (start + i) * count

    return total


#print(range_addition(2, 2, 5))
