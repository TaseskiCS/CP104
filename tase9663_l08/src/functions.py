"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports

# Constants

# t03


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    list = ['zero',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine'

            ]
    return list[n]


# print(get_digit_name(3))


# t06

def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = values[0]
    largest = values[0]
    total = 0

    for value in values:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value

        total += value

    average = total / len(values)

    return smallest, largest, total, average


#print(list_stats([94, 96, -22, -79, -28, -26, -50, 71, 24, -32]))


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    list = []
    for i, v in enumerate(values):
        if v == value:
            list.append(i)

    return list


#print(many_search([94, 96, -22, -79, -28, 96, -50, 71, 24, -32], 96))

def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    for v1, v2 in zip(source1, source2):
        sum = v1 + v2
        target.append(sum)

    return target


#print(list_sums([10, 3, 10, 3, 1], [8, 2, 7, 3, 6]))
# case output: [18, 5, 17, 6, 7]

def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    for v1 in source1:
        for v2 in source2:
            if v1 == v2 and v1 not in target:
                target.append(v1)

    return target


#print(intersection([10, 3, 10, 3, 1], [8, 2, 7, 3, 6, 10, 32, 99]))
