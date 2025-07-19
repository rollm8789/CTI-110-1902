# About
# Name: Firstname Lastname
# Date: July 7, 2025
# Homework: P4LAB1a - Shapes
# Description: This program uses Python's turtle graphics to draw a square and a triangle.
#              It uses a for loop for the square and a while loop for the triangle.
#              The turtle cursor is set to a turtle shape, and the shapes are drawn
#              in separate positions to avoid overlap.

import turtle

# Set up the turtle
t = turtle.Turtle()
t.shape("turtle")  # Set cursor to turtle shape
t.speed(5)

# Draw a square using a for loop
for i in range(4):
    t.forward(100)
    t.right(90)

# Move to a new position for the triangle without drawing
t.penup()
t.goto(150, 0)  # Move right to separate shapes
t.pendown()

# Draw a triangle using a while loop
sides = 3
while sides > 0:
    t.forward(100)
    t.left(120)
    sides -= 1

# Keep the window open
turtle.done()