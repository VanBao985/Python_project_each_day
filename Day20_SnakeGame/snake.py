from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]

UP, LEFT, DOWN, RIGHT = 90, 180, 270, 0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for x, y in positions:
            self.add_segment(x, y)
    
    #function occurs when snake detect collision with food
    def extends(self):
        (x_new, y_new) = self.segments[len(self.segments)-1].pos()
        self.add_segment(x_new, y_new)

    def add_segment(self, x, y):
        turtle = Turtle("square")
        turtle.color("white")
        # turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        self.segments.append(turtle)
    
    #snake default forward 20 pixels after 0.1s
    def move(self):
        index = list(range(len(self.segments)))
        for idx in index[:0:-1]:
            (x_new, y_new) = self.segments[idx-1].pos()
            self.segments[idx].goto((x_new, y_new))
        self.head.forward(20)

    def game_over(self):
        self.segments.clear()
        self.head.goto(10000, 10000)

    #list function controls snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)