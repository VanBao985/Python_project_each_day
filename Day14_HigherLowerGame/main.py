from pandas import read_json
import random as rd
from art import logo, vs
from replit import clear
from time import sleep

df = read_json("Day14_HigherLowerGame/data.json")

clear()
score = 0
while True:
    print(logo)
    # Generate a random account from the game data.
    object_1 = df.loc[rd.randint(0, len(df)-1)]
    object_2 = df.loc[rd.randint(0, len(df)-1)]
    
    #print 2 object about name, description, country and hide follower_count
    print(f"Object 1: Name {object_1["name"]}, with description: {object_1["description"]} and from {object_1["country"]}")
    sleep(0.5)
    print(vs)
    sleep(0.5)
    print(f"Object 2: Name {object_2["name"]}, with description: {object_2["description"]} and from {object_2["country"]}")
    print()
    ans = (input("Compare number of followers on instagram, higher or lower? Input H or L:  ")).lower()
    if object_1["follower_count"] > object_2["follower_count"]:
        if ans == "h":
            score += 1
            print(f"Answer correct! Score: {score} The next question: ")
        else:
            print("Sorry, answer incorrect!")
            break
    else:
        if ans == "l":
            score += 1
            print(f"Answer correct! Score: {score} The next question: ")
        else:
            print("Sorry, answer incorrect!")
            break
    sleep(1)


print("Say goodbye!")

