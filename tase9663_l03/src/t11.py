"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-09-27"
-------------------------------------------------------
"""
# Imports

# Constants
LEFT = "left"
MIDDLE = "middle"
RIGHT = "right"
WIDTH = 20  # Each line in given output had a 20 space so here we define it

# OUTPUTS
print(f"{LEFT:-<{WIDTH}s}")

print(f"{MIDDLE:-^{WIDTH}s}")

print(f"{RIGHT:->{WIDTH}s}")
