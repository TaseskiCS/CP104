"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-19"
-------------------------------------------------------
"""
# Constants
SECONDS_PER_MINUTE = 3600
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

# Take user input in seconds
time = int(input("Number of seconds: "))

# TODO: user input calculation in seconds converted to days using floor division and ${SECONDS_PER_MINUTE} Constant
days = time // (HOURS_IN_DAY * SECONDS_PER_MINUTE)
time = time % (HOURS_IN_DAY * SECONDS_PER_MINUTE)
hours = time // SECONDS_PER_MINUTE
time %= SECONDS_PER_MINUTE
minutes = time // MINUTES_IN_HOUR
time %= MINUTES_IN_HOUR
seconds = time

# Outputs
print(f'Days: {days} Hours: {hours} Minutes: {minutes} Seconds: {seconds}')
