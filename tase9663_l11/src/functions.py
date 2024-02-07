"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""
# Imports
import random
# Constants


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """

    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            if value_type == 'float':
                row.append(random.uniform(low, high))
            else:
                row.append(random.randint(low, high))
        matrix.append(row)

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """

    if value_type == "float":
        count_row = 0

        for i in range(len(matrix)):
            count_row += 1
            count_col = 0
            for j in range(len(matrix[i])):
                count_col += 1

        for i in range(count_col):
            if i == count_col - 1 and i == 0:
                print(f"{i:9d}")
            elif i == 0:
                print(f"{i:9d}", end="")
            elif i == count_col - 1:
                print(f"{i:7d}")
            else:
                print(f"{i:7d}", end="")

        for i in range(count_row):
            print(f"{i:2d}", end="")
            for j in range(count_col):
                print(f"{matrix[i][j]:7.2f}", end="")
            print()

    else:
        count_row = 0

        for i in range(len(matrix)):
            count_row += 1
            count_col = 0
            for j in range(len(matrix[i])):
                count_col += 1

        for i in range(count_col):
            if i == 0 and i == count_col - 1:
                print(f"{i:9d}")
            elif i == 0:
                print(f"{i:9d}", end="")
            elif i == count_col - 1:
                print(f"{i:7d}")
            else:
                print(f"{i:7d}", end="")
        for i in range(count_row):
            print(f"{i:2d}", end="")
            for j in range(count_col):
                print(f"{matrix[i][j]}", end="")
            print()

    return None


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]

    s_loc = [0, 0]
    l_loc = [0, 0]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            # if each value it iterates through is less than smallest than append
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]
                s_loc = [i, j]
            elif matrix[i][j] > largest:
                largest = matrix[i][j]
                l_loc = [i, j]

    return s_loc, l_loc


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= num


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transposed.append(new_row)

    return transposed
