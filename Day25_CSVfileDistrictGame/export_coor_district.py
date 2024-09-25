import turtle

#set up turtle and image to click same the main.py
screen = turtle.Screen()
image = "Day25_CSVfileDistrictGame/DistrictHaNoi.gif"
screen.addshape(image)
screen.setup(width=900, height=650)
screen.title("District of HaNoi")
tim = turtle.Turtle()
tim.shape(image)


coor = []
#function click to get x, y coordinate and add to list
def get_mouse_click_coor(x, y):
    # turtle.onscreenclick(None)
    coor.append((x, y))
    #click enough 30 districts then print coor list to get data
    if len(coor) == 30:
        print(coor)

turtle.onscreenclick(get_mouse_click_coor)

screen.mainloop()
