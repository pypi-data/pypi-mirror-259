import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Set animation speed (0 is fastest)
t.pensize(4)
t.color("white")

# Write Hello World with animation
t.penup()
t.goto(-100, 0)
t.pendown()
for char in "Hello World!":
    t.write(char, align="center", font=("Courier", 34, "bold"))
    t.forward(50)

# Keep the window open
turtle.done()
