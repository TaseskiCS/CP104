"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Antonio Taseski
ID:     169069663
Email:  tase9663@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌‌​​‌‌​​​‌​‌‌‌‌‌:
        altered - the resulting string (str)
    -------------------------------------------------------
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    altered = ''
    for k, v in enumerate(string):
        if v in vowels:
            altered += string[k].upper()
        else:
            altered += string[k]

    return altered
