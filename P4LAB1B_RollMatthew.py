# About
# Name: Matthew Roll
# Date: 7-7-2025
# Homework: P4LAB1b - Initials
# Description: This program uses Python's turtle graphics to draw the initials "M" and "R"
#              in a proper writing format, side by side. The turtle uses a blue pen with
#              a size of 3, and the initials are drawn without overlapping, with "R" positioned
#              to the right of "M" at the same vertical level.

import turtle

# Set up the turtle
t = turtle.Turtle()
t.shape("turtle")  # Set cursor to turtle shape
t.speed(5)
t.pencolor("blue")  # Set color to blue
t.pensize(3)       # Set pen size

# Draw first initial (M)
t.left(90)         # Point up
t.forward(50)      # Draw left vertical line of M
t.right(135)       # Angle for first diagonal
t.forward(35.36)   # Draw diagonal down (sqrt(25^2 + 25^2) = 35.36 for 45-degree angle)
t.left(90)         # Angle for second diagonal
t.forward(35.36)   # Draw diagonal up
t.right(135)       # Point up again
t.forward(50)      # Draw right vertical line of M

# Move to position for second initial (R)
t.penup()
t.goto(60, 0)      # Move right to draw R, starting at same y-level (y=0)
t.setheading(0)    # Reset orientation to face right
t.pendown()

# Draw second initial (R)
t.left(90)         # Point up
t.forward(50)      # Draw vertical line of R
t.right(90)        # Point right
t.forward(25)      # Draw top horizontal line of R
t.right(90)        # Point down
t.forward(25)      # Draw middle vertical line to start loop
t.right(90)        # Point left
t.forward(25)      # Draw bottom of loop
t.left(90)         # Point up

t.left(45)         # Angle for diagonal leg
t.forward(35.36)   # Draw diagonal leg to base (sqrt(25^2 + 25^2) = 35.36)

# Keep the window open
turtle.done()
