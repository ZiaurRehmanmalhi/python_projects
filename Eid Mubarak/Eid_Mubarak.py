import turtle
import random

screen = turtle.Screen()
screen.bgcolor("#000000")

colors = ["#ffffff", "#ff6600", "#ffff00", "#00ff00", "#0080ff", "#8000ff"]
font = ("Arial", 100, "bold")


def glow():
    t.pensize(random.randint(5, 30))
    t.pencolor(colors[random.randint(0, 5)])
    t.forward(50)
    t.right(144)


t = turtle.Turtle()
t.speed(0.5)
t.penup()
t.goto(0, 0)
t.pendown()

# Write the "Eid Mubarak" message
t.pencolor("#00bfff")
t.write(" Eid Mubarak\n To All Team", font=font, align="center")

for i in range(10):
    t.penup()
    t.goto(random.randint(-430, 400), random.randint(-300, 300))
    t.pendown()
    t.pensize(random.randint(5, 30))
    t.pencolor(colors[random.randint(0, 5)])
    for j in range(50):
        t.forward(50)
        t.right(144)

while True:
    glow()
