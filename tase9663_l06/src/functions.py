"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-10-26"
-------------------------------------------------------
"""
# Imports

# Constants

WEEK_PERIOD = 6


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """

    total = 0
    for i in range(start, finish + 1, increment):
        total += i
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(1, height + 1):
        print((height - i) * ' ' + char * (2 * i - 1))

    return None


def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, width + 1):
        if i == 1 or i == width:
            print(char*i)
        else:
            print((char + ' ' * (i-2) + char))

# t08


# draw_hollow_triangle(8, '#')


# t11

def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    increase /= 100  # convert to decimal
    text_salary = "Salary"
    print(f"Age{text_salary:>16}")
    line = ''
    print(f'{line:->19}')
    for i in range(age, 65+1):
        print(f"{i:<10}{salary:>9,.2f}")
        salary += salary * increase

    return None


#retirement(60, 40, 100.0)


# t13

def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    # sample usage lumber(2, 10, 2, 2, 12, 2)
    # for i in range(b_min, b_max, b_inc):
    print(f"{'Cross-Sectional':>30} {'Moment Of':>12} {'Section':>9}")
    print(f"{'Base':>4} {'Height':>7} {'Area':>6} {'Inertia':>21} {'Modulus':>11}")
    line = ''
    print(f'{line:->53}')

    for b in range(b_min, b_max + 1, b_inc):
        for h in range(h_min, h_max + 1, h_inc):
            area = b * h
            inertia = b * h ** 3 / 12
            modulus = b * h ** 2 / 6
            print(f"{b:4}  x {h:4} {area:18.2f} {inertia:11.2f} {modulus:9.2f}")

    return None


#lumber(2, 10, 2, 2, 12, 2)


# t14

def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    total_hours = 0
    for w in range(1, WEEK_PERIOD+1):
        print(f'Week {w}')
        for i in range(1, ia_count+1):
            marking_hours = float(input(f'Marking Hours for IA {i}: '))

            total_hours += marking_hours

    return total_hours


# print(ia_hours(3))


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------
    Parameters:
        n - number of verses of the song to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(n, 0, -1):
        amount = 'bottle' if i == 1 else 'bottles'
        print(f"{i} {amount} of beer on the wall, {i} {amount} of beer.")
        print(
            f"Take one down, pass it around, {i-1 if i-1 else 'no more'} {amount} of beer on the wall.\n")

    return None

# t08


# bottles_of_beer(99)
