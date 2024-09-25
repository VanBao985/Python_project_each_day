from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sco = 0
        with open ("Day20_SnakeGame/highscore.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.write(f"Score: {self.sco}  High score: {self.high_score}", align= ALIGNMENT, font= FONT)

    #snake detect collision food
    def update_score(self):
        self.sco +=1
        self.clear()
        self.write(f"Score: {self.sco}  High score: {self.high_score}", align= ALIGNMENT, font= FONT)

    def update_highscore(self):
        if self.sco > self.high_score:
            self.high_score = self.sco
            with open("Day20_SnakeGame/highscore.txt", mode="w") as data:
                data.write(str(self.high_score))

    def game_over(self):
        self.home()
        self.write(f"Game over! Score: {self.sco}", align=ALIGNMENT, font=FONT)
