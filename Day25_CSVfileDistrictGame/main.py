import pandas as pd
from turtle import Turtle, Screen


df = pd.read_csv("Day25_CSVfileDistrictGame/District.csv")
data = df.to_dict()

screen = Screen()
image = "Day25_CSVfileDistrictGame/DistrictHaNoi.gif"
screen.addshape(image)
screen.setup(width=900, height=650)
screen.title("District of HaNoi")

turtle = Turtle()
# turtle.hideturtle()
turtle.shape(image)


#logic game
cnt = 0

while cnt < 30: 
    ans_user = screen.textinput(title=f"{cnt}/30 Guessed correctly!", prompt="Input name of the district: ").title()
    for idx in range(len(df)):
        if data["District"][idx] == ans_user:
            tim = Turtle()
            tim.hideturtle()
            tim.penup()
            # tim.color("red")
            tim.goto(data["x"][idx], data["y"][idx])
            FONT = "Courier", 8, "normal"
            tim.write(ans_user, align="center", font= FONT)
            cnt+=1


screen.exitonclick()