from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time 

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

game_is_on = True

def game_over():
    score.game_over()
    snake.game_over()
    score.update_highscore()
    # global game_is_on
    # game_is_on == False


#control direct of snake
screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")


while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    

    #snake detect collision food
    if snake.head.distance(food) < 0.1:
        food.renew()
        snake.extends()
        score.update_score()

    #snake detect collision wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_over()
    
    #snake detect collision tail
    for seg in snake.segments:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game_over()
    





screen.exitonclick()