"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants
TAX_SALARY = 0.03625
OVERTIME_RATE = 1.5

# t01


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0
    guess = int(input('Guess: '))
    count += 1
    while guess != number:
        count += 1
        if guess > number:
            print('Too high, try again.')
        elif guess < number:
            print('Too low, try again.')
        guess = int(input('Guess: '))
    print('Congratulations - good guess!')
    print(f'You made {count} guesses.')

    return count


# hi_lo_game(100)

# t02
def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """

    # if target == 0:
    #     power = 1

    power = 1
    while power < target:
        power *= 2
    return power


# print(power_of_two(248))

# t04
def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    total = 0
    num = 0
    while total <= target:
        num += 1
        total += num * num
    return total


# print(sum_squares(26))


# def num_categories():
#     """
#     -------------------------------------------------------
#     Asks a user to enter a series of numbers, then counts and returns
#     how may positives, negatives, and zeroes there are.
#     Stop processing values when the user enters -999.
#     Use: negatives, zeroes, positives = num_categories()
#     -------------------------------------------------------
#     Returns:
#         negatives - number of negative values (int)
#         zeroes - number of zero values (int)
#         positives - number of positive values (int)
#     ------------------------------------------------------
#     """
#     negatives = 0
#     zeroes = 0
#     positives = 0
#     loop = True
#     first = float(input('Enter First Value: '))
#     if first == -999:
#         loop = False
#     if first < 0 and first != -999:
#         negatives += 1
#     elif first == 0:
#         zeroes += 1
#     elif first > 0:
#         positives += 1
#
#     while loop == True:
#         next = float(input('Enter Next Value: '))
#
#         if next == -999:
#             loop = False
#             break
#
#         if next < 0:
#             negatives += 1
#         elif next == 0:
#             zeroes += 1
#         elif next > 0:
#
#             positives += 1
#
#     return negatives, zeroes, positives


# print(num_categories())


# def meal_costs():
#     """
#     -------------------------------------------------------
#     Asks a user the costs of breakfast, lunch, and supper for each
#     day the user was away. Assumes there is at least one day, and
#     after entering data for each day asks the user whether they want
#     to enter data for another day. Calculates total costs for meals.
#     Use: b_total, l_total, s_total, a_total = meal_costs()
#     -------------------------------------------------------
#     Returns:
#         b_total - total breakfasts cost (float)
#         l_total - total lunches cost (float)
#         s_total - total suppers cost (float)
#         a_total - all meals cost (float)
#     ------------------------------------------------------
#     """
#
#     day = 1
#     b_total = 0
#     l_total = 0
#     s_total = 0
#     a_total = 0
#
#     while True:
#         print(f'For Day {day}')
#
#         breakfast = float(input('How much was breakfast? '))
#         lunch = float(input('How much was lunch? '))
#         supper = float(input('How much was supper? '))
#         day_total = breakfast + lunch + supper
#         print(f'Your total for the day was: {day_total}')
#
#         b_total += breakfast
#         l_total += lunch
#         s_total += supper
#         a_total += lunch + breakfast + supper
#
#         away_check = str(input('Were you away for another day? (Y/N) '))
#         if away_check == 'Y':
#             day += 1
#         else:
#             break
#
#     return b_total, l_total, s_total, a_total


# print(meal_costs())
# t08


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = 0
    expense = float(input('Enter an expense (0 to quit): '))
    expenses += expense
    balance = available - expenses - expense
    while expense != 0:
        expense = float(input('Enter another expense (0 to quit): '))

        expenses += expense
        balance = available - expenses - expense

    if expenses > available:
        status = 'Deficit'
    elif expenses < available:
        status = 'Surplus'
    elif expenses == available:
        status = 'Balanced'

    return expenses, balance, status


# print(budget(200))


# t10

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    loop = True
    pay_total = 0
    total = 0  # total wages
    emp_num = 0
    while loop:
        id = int(input('Employee ID: '))
        if id == 0:
            loop = False
            break
        emp_num += 1
        hour_wage = float(input('Hourly Wage Rate: '))
        hours_worked = float(input('Hours Worked: '))
        NORMAL_PAY = 40*hour_wage
        if hours_worked > 40:
            OVERTIME_PAY = hour_wage * OVERTIME_RATE * \
                (hours_worked - 40)
            pay_total = NORMAL_PAY + OVERTIME_PAY
        else:
            pay_total = hour_wage * hours_worked
        taxed_total = pay_total * TAX_SALARY
        pay_total -= taxed_total
        print(f'Net payment for employee {id}: ${pay_total:,.2f}')
        print()

        total += pay_total
    average = total / emp_num
    return total, average


# total, average = employee_payroll()
#
# print(total, average)
