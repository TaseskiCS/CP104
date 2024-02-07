"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports

# Constants


def total_wins():
    """
    -------------------------------------------------------
    Asks the user to enter a series of strings representing game outputs.
    The function continues to prompt the user until an empty string is entered.
    Counts the occurrences of "purple" and "gold" in the input strings.
    Use: purple_count, gold_count = total_wins()
    -------------------------------------------------------
    Returns:
        purple_count - the number of times "purple" appeared in the input (int)
        gold_count - the number of times "gold" appeared in the input (int)
    -------------------------------------------------------
    """
    purple = 0
    gold = 0

    while True:
        prompt = str(input('Enter the winning team: '))
        if prompt == '':
            break

        if prompt == 'purple':
            purple += 1
        elif prompt == 'gold':
            gold += 1

    return purple, gold


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    divisor = 2
    prime = True
    if number <= 1:
        prime = False

    while divisor <= number // 2:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1

    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    # Convert interest_rate to a decimal
    interest_rate /= 100

    # Print loan details
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2%}")
    print(f"Monthly Payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month   Interest   Payment   Balance")
    print("----------------------------------")

    # Initialize variables
    month = 1
    balance = principal_amount

    while balance > 0:
        interest = balance * (interest_rate / 12)

        if payment > balance + interest:
            payment = balance + interest

        balance -= payment - interest

        print(
            f"    {month:2}     {interest:.2f}    {payment:.2f}    {balance:.2f}")

        month += 1

    return None


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """

    digits = 0

    number = abs(number)
    # Use repeated division by 10 to count the digits
    while number > 0:
        number //= 10
        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    # Initialize the total and the divisor
    total = 0
    divisor = 1

    # Use a while loop to iterate through potential factors
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    return total
