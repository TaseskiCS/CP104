"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-11-14"
-------------------------------------------------------
"""
# Imports

# Constants


def list_factors(number):
    """
    -------------------------------------------------------
    Returns a list of the factors that make up the target number 
    excepting the number itself.
    User: list = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - number greater than 0 (int)
    Returns:
        factors - list of numbers that make up {number} without
        the {number} included (list of int)
    -------------------------------------------------------
    """

    factors = []

    for i in range(number):
        if i > 0:
            if number % i == 0:
                if i not in factors:
                    factors.append(i)

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    number_list = []
    while True:
        num = int(input('Enter a positive number: '))
        if num == 0:
            break
        elif num > 0:
            number_list.append(num)

    return number_list


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    for k, v in enumerate(numbers):
        if v == target_number:
            index_list.append(k)
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in minuend:
        if i not in subtrahend:
            minuend[:] = [i]
    return None


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            in_order = False
            index = i
    return in_order, index
