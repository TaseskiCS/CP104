"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports

# Constants


def file_top(file_handle, count):
    """
    Prints first count lines of file_handle. Line numbering starts at 0.
    If the length of the file is shorter than count, stops printing after
    the last line of the file.

    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    """
    i = 0
    while i < count:
        line = file_handle.readline().strip()
        if not line:
            break
        print(line)
    return None


def read_integers(file_handle):
    """
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.

    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    """
    content = file_handle.read()
    tokens = content.split(',')
    number_list = [int(token) for token in tokens if token.strip().isdigit()]
    return number_list


def file_statistics(file_handle):
    """
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (including end-of-line
    characters), and remaining characters.

    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    """
    content = file_handle.read()

    ucount = sum(1 for char in content if char.isupper())
    lcount = sum(1 for char in content if char.islower())
    dcount = sum(1 for char in content if char.isdigit())
    wcount = sum(1 for char in content if char.isspace())
    rcount = len(content) - (ucount + lcount + dcount + wcount)

    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.

    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    """
    line_number = 0
    for line in fh_read:
        fh_write.write(f"[{line_number}] {line}")
        line_number += 1

    return None


def student_stats(file_handle):
    """
    Get information from a file of file_handle and grades.

    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    """
    total_marks = 0
    num_students = 0
    min_mark = float('inf')
    max_mark = float('-inf')
    l_id = h_id = None

    for line in file_handle:
        _, _, student_id, mark_str = line.strip().split(',')
        mark = float(mark_str)

        total_marks += mark
        num_students += 1

        if mark < min_mark:
            min_mark = mark
            l_id = student_id

        if mark > max_mark:
            max_mark = mark
            h_id = student_id

    avg = total_marks / num_students if num_students > 0 else 0

    return l_id, h_id, avg


def words_to_matrix(word_list):
    """
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)

    Parameters:
        word_list - a list containing the words to be placed in
                    the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
                 in word_list (2D list of string).
    """
    # Check if the word_list is empty
    if not word_list:
        return []

    # Ensure all words have the same length
    word_length = len(word_list[0])
    if not all(len(word) == word_length for word in word_list):
        raise ValueError("All words must be the same length.")

    # Create a 2D list of characters using nested loops
    matrix = []
    for i in range(word_length):
        new_column = []
        for word in word_list:
            new_column.append(word[i])
        matrix.append(new_column)

    return matrix


# Example usage:
word_list = ["cat", "dog", "big"]
matrix_result = words_to_matrix(word_list)
print(matrix_result)
