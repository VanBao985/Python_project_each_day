from turtle import Turtle, Screen
import random as rd

#color (r, g, b) r,g,b  range 1-255, tuple(r,g,b) set only color
def rd_color():
    r = rd.randint(1, 255)
    g =rd.randint(1, 255)
    b = rd.randint(1, 255)
    return (r, g, b)

turtle = Turtle()
colors = ["aquamarine", "blue4", "brown3", "chocolate2", "MediumSlateBlue", "OliveDrab4", "PaleGreen2", "PowderBlue"]
turtle.pensize(5)
directions = [0, 90, 180, 270]


for _ in range(100):
    turtle.forward(40)
    color = rd.choice(colors)
    turtle.color(rd_color())
    turtle.setheading(rd.choice(directions))



#show result come out
screen = Screen()
screen.exitonclick()