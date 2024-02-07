"""
-------------------------------------------------------
Exam Task 5 Function Definitions
-------------------------------------------------------
Author: Antonio Taseski
ID:     169069663
Email:  tase9663@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def fill_matrix(fh_in, rows, cols):
    """
    -------------------------------------------------------
    Creates a rows by cols 2D list of integers filled with
    space-separated integers from f_in. If f_in does not have enough values,
    fill the remaining slots with 0s. If f_in has too many values,
    the excess values are ignored.
    Use: matrix = fill_matrix(fh_in, rows, cols)
    -------------------------------------------------------
    Parameters:
        fh_in - the integers file to process (file handle - already open for reading)
        rows - rows in matrix (int > 0)
        cols - columns in matrix (int > 0)
    Returns‌​‌​​​​‌​​‌‌‌‌​​‌‌​​​‌​‌‌‌‌‌:
        matrix - a 2D list of integers (2D list of int)
    -------------------------------------------------------
    """

    # Your code here
    matrix = []
    vals = []

    for x in range(rows):
        line = fh_in.readline()
        row = line.strip().split()
        for y in range(len(row)):
            vals.append(row[y])
        row = []
        for i in range(cols):
            try:
                row.append(int(vals[i+(x*cols)]))
            except:
                row.append(0)

        matrix.append(row)
    return matrix
