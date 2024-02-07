"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Antonio Taseski
ID:      169069663
Email:   tase9663@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants

# Inputs
foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
cost_concrete_per_m3 = float(input("Cost of concrete ($/m^3): "))
cost_bricks_per_m2 = float(input("Cost of bricks ($/m^2): "))

# volume of concrete needed for the foundation
foundation_volume = foundation_length * foundation_width * foundation_height

# cost of concrete
cost_concrete_foundation = cost_concrete_per_m3 * foundation_volume

# surface area of the walls
wall_area = 2 * (foundation_length * wall_height +
                 foundation_width * wall_height)

# amount of bricks needed for the walls
bricks_needed = wall_area

# cost of bricks
cost_bricks_walls = cost_bricks_per_m2 * wall_area

# total cost
total_cost = cost_concrete_foundation + cost_bricks_walls

# Outputs
print(f"Concrete needed for foundation (m^3): {foundation_volume:.2f}")
print(f"Cost of concrete: ${cost_concrete_foundation:,.2f}")
print(f"Bricks needed for walls (m^2): {wall_area:.2f}")
print(f"Cost of bricks: ${cost_bricks_walls:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
