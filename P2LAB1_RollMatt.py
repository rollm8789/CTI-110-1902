# Matthew Roll
# 2025-06-23
# P2LAB1 - Circle Calculations
# This program calculates and displays the diameter, circumference, and area of a circle
# based on a user-provided radius. The results are formatted to specific decimal places.

import math

# Get radius from user
radius = float(input("Enter the circle's radius: "))

# Perform calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
