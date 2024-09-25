from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.color("blue")
        self.renew()
    
    #function occurs when snake detect collision with food
    def renew(self):
        x_food = rd.randint(-14, 14) * 20
        y_food = rd.randint(-14, 13) * 20
        self.goto(x_food, y_food)