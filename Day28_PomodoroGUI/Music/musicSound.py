from pygame.mixer import music
import pygame
import pandas as pd
import random as rd

# Initial pygame
pygame.mixer.init()


#------------ load music study --------------------\
def music_study():
    # load playlist music from file csv and add to path 
    df = pd.read_csv("Music/music_study.csv").to_dict()
    name_music = df['music'][rd.randint(1, len(df['music'])-1)]
    path_music = "Music/"+name_music+".mp3"
    # print(path_music)
    music.load(path_music)
    music.play()

#------------ load music study --------------------
def music_break():
    music.load("Music/break.mp3")
    music.play()

# ----------- pause music ------------------
def pause_music():
    music.pause()

def unpause_music():
    music.unpause()

#------------ stop music --------------------
def stop_music():
    # time.sleep(10)
    music.stop()


# music_study()
# music_break()