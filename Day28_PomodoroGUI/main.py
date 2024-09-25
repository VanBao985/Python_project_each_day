from tkinter import *
from infoPomodoro import show_info
import math
from tkinter import simpledialog
from Music.musicSound import music_study, music_break, stop_music, pause_music, unpause_music
from random import randint
from pygame.mixer import music


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FIREBRICK1 = "#FF3030"
FONT_NAME = "Courier"
FONT_BUTTON = (FONT_NAME, 12, "bold")
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 15
reps = 1
#Timer of window
Timer = None
time_pause = 0

#Mode: 50-10 or 25-5
OPTION50 = 60 #60 * 50 (s) = 50min
OPTION25 = 30 #30 * 50 (s) = 25min
OPTION = 60 #default 50min

# ---------------------------- TIMER STOP ------------------------------- # 
def stop():
    stop_music()
    canvas.itemconfig(timer_label,text="STOP!")
    global reps
    reps = 1
    global Timer
    window.after_cancel(Timer)
    global time_pause 
    time_pause = 0 #reset time


# ---------------------------- TIMER PAUSE ------------------------------- # 
def pause():
    pause_music()
    canvas.itemconfig(timer_label,text="PAUSE!")
    global reps
    reps -=1
    global Timer
    window.after_cancel(Timer)
    # Timer = None


# ---------------------------- TIMER MECHANISM --------------------------- # 
def start():    
    global reps
    time_count = 0 
    if reps % 8 == 0: 
        canvas.itemconfig(timer_label,text="LONG BREAK")
        time_count = LONG_BREAK_MIN * OPTION
    elif reps % 2 == 0:
        canvas.itemconfig(timer_label,text="BREAK")
        time_count = SHORT_BREAK_MIN * OPTION
    else: 
        canvas.itemconfig(timer_label,text="STUDY")
        time_count = WORK_MIN * OPTION
    #func continue when paused
    if time_pause > 0:
        unpause_music()
        time_count = time_pause
    else:
        if reps % 2 == 0 and reps != 0:
            music_break()
        else:
            quote_label.config(text=quote())
            music_study()

    countdown(time_count)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time):
    global time_pause
    time_pause = time
    count_min = math.floor(time/60)
    count_sec = time % 60
    # complete = all be completed when long break except the first, reps = 1
    if reps % 8 == 1 and reps != 1: 
        check_marks.config(text="All be completed!")
    if reps % 8 == 2:
        check_marks.config(text="Completed: 0")

    if count_sec < 10:
        count_sec = '0' + str(count_sec)
    if time >= 0:
        canvas.itemconfig(time_show, text= f"{count_min}:{count_sec}")
        global Timer
        Timer = window.after(1000, countdown, time-1)
    else: 
        marks = "Complete:"
        for _ in range(int((reps%8)/2)):
            marks += "✓"
        check_marks.config(text=f"{marks} _")
        start()

#--------CHANGE MODE--------
mode = 0
def change_option():
    global mode
    info_mode ="1. Work: 50; Break: 10 - 15 min \t2. Work: 25; Break: 5 -7.5min \nPlease STOP clock before changing!! \nInput 1 or 2 to select suitable mode for you"
    mode = simpledialog.askinteger("Change mode", info_mode)
    global OPTION
    if mode == 1:
        OPTION = OPTION50
        canvas.itemconfig(time_show, text="50:00")
    elif mode == 2:
        OPTION = OPTION25
        canvas.itemconfig(time_show, text="25:00")
    else: 
        pass


# -------------------- read file quote ---------------------
def quote():
    length = 0
    with open("Quote/quote.txt") as file:
        for _ in file:
            length += 1
    with open("Quote/quote.txt") as file:
        quote = file.readlines()
    numrd = randint(1, length-1)
    sol = quote[numrd].strip()
    return sol


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Practice with Pomodoro")
window.config(padx=30, pady=10, bg=YELLOW)
window.iconbitmap("Image/pomodoro-technique.ico")

#canvas
canvas = Canvas(width=202, height=240, bg=YELLOW, highlightthickness=0)
# image_path = os.path.join(os.path.dirname(__file__), "tomato.png")

tomato_img = PhotoImage(file = "Image/tomato.png")
canvas.create_image(102, 120, image=tomato_img)

time_show = canvas.create_text(102, 164, text="50:00", font=(FONT_NAME, 30, "bold"), fill="white")


#timer label
timer_label = canvas.create_text(102, 115, text="Pomodoro", font=(FONT_NAME, 26, "bold"), fill="darkgreen")
# Label(text="Pomodoro", font=(FONT_NAME, 20, "bold"), bg="red", fg= "darkgreen")
# timer_label.grid(column=1, row=1)

canvas.grid(column=1, row=1)

#test countdown
# countdown(20)


#start, pause, stop button
start_button = Button(text="Start", font=FONT_BUTTON, fg=FIREBRICK1, command=start)
start_button.grid(column=0, row=2)

stop_button = Button(text="Pause", font=FONT_BUTTON, fg=FIREBRICK1, command=pause)
stop_button.grid(column=1, row=2)

stop_button = Button(text="Stop", font=FONT_BUTTON, fg=FIREBRICK1, command=stop)
stop_button.grid(column=2, row=2)

#check mark label 
check_marks = Label(text="Complete: 0", font=(FONT_NAME, 20, "bold"), fg="forestgreen", bg=YELLOW, highlightthickness=0)
# check_marks.config(pady=10)
check_marks.grid(column=0,row=0, columnspan=3)

#Quote to work hard:
quote_label = Label(text=quote(), wraplength=360, font=(FONT_NAME, 11, "italic"), fg="darkgreen", bg=YELLOW, highlightthickness=0)
quote_label.grid(row=3, column=0, columnspan=3, rowspan=2)

#button show detail message 
detail_button = Button(text="Detail", command=show_info, font=(FONT_NAME, 8, "bold"), fg="#1E90FF")
detail_button.grid(row=5, column=2)

#button change option
change_button = Button(text="Mode", command=change_option, font=(FONT_NAME, 8, "bold"), fg="#1E90FF")
change_button.grid(row=5, column=0)


#update function: customize volume music 
def customize_volume(value):
    vol = float(value)/100
    music.set_volume(vol)

scale = Scale(from_=100, to=0, command=customize_volume, bg=YELLOW, fg="lightcoral", highlightthickness=0)
scale.grid(row=1, column=2, sticky="n", pady=70)

vol_label = Label(text="Volume", font=(FONT_NAME, 11, "bold"), fg="darkgreen", bg=YELLOW, highlightthickness=0)
vol_label.grid(row=1, column=2, sticky="s", pady=50)


window.mainloop()