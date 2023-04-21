import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("#000000")

# Define the colors and font
colors = ["#ffffff", "#ff6600", "#ffff00", "#00ff00", "#0080ff", "#8000ff"]
font = ("Arial", 60, "bold")

# Define the function to create the glowing effect
def glow():
    t.pensize(random.randint(5, 30))
    t.pencolor(colors[random.randint(0, 5)])
    t.forward(50)
    t.right(144)

# Create the turtle object
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, 0)
t.pendown()

# Write the "Eid Mubarak" message
t.pencolor("#00bfff")
t.write("Eid Mubarak", font=font, align="center")

# Loop to create the glowing effect
while True:
    glow()
