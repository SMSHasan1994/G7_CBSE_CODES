# Drawing a ractangle using Sequence Program
import turtle

# Create a turtle object
t = turtle.Turtle()

# Set pen color and width
t.pencolor("red")
t.pensize(5)

# Draw the rectangle using sequence program
t.forward(50)
t.right(90)
t.forward(30)
t.right(90)
t.forward(50)
t.right(90)
t.forward(30)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
