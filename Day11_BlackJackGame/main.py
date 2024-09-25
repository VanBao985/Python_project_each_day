############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


import random as rd
from replit import clear
from art import logo
from time import sleep

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return rd.choice(cards)

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) 
    #and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    s = sum(cards)
    if s == 21 and len(cards) == 2:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, 
    #remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if s > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. 
# If the computer and user both have the same score, then it's a draw. If the computer has 
# a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. 
# If the user_score is over 21, then the user loses. If the computer_score is over 21, 
# then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == 0 and computer_score == 0:
        print("Draw!")
    elif user_score == computer_score:
        print("Draw!")
    elif user_score == 0: 
        print("You have a blackjack, you winnnnnn!")
    elif computer_score == 0: 
        print("Computer has a blackjack, you lose ^^ ")
    elif computer_score > 21: 
        print("You win")
    elif computer_score > user_score:
        print("You lose")
    else:
        print("You win!")

#function to restart game. delete computer, user card...
def restart():
    clear()
    user_card.clear()
    computer_card.clear()


#Hint 5: Deal the user and computer 2 cards each using deal_card()
user_card = []
computer_card = []
is_game_over = False


#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or 
#if the user's score is over 21, then the game ends.
#Hint 11: The score will need to be rechecked with every new card drawn and 
#the checks in Hint 9 need to be repeated until the game ends.
while is_game_over == False:
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    print(logo)
    if calculate_score(computer_card) == 0 or calculate_score(user_card) > 21:
        is_game_over = True
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. 
    #If yes, then use the deal_card() function to add another card to the user_cards List. 
    #If no, then the game has ended.
    print(f"Your have cards {user_card}, with {calculate_score(user_card)} score")
    print(f"Computer have a card: {computer_card[0]}, and another card be hiden")
    while calculate_score(user_card) <= 21:
        sleep(0.5)
        print("Do you want to get another card, carefully!!  input y to receive or n to deny")
        inp = input().lower()
        if inp == 'y':
            user_card.append(deal_card())
            print(f"Your have cards {user_card}, with {calculate_score(user_card)} score")
            #if user score > 21, lose, is_game_over = true, break out loop through
            if calculate_score(user_card) > 21:
                print("OHH! Over 21. You lose!")
                is_game_over = True
                break
        else:
            break
    #if user score <= 21, game continue, else ends
    if is_game_over == False:    
        sleep(0.5)
        print("OK! Your cards are finally. Good luck")
        #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep 
        #drawing cards as long as it has a score less than 17.
        sleep(1)
        print(f"Computer's cards: {computer_card}")
        while calculate_score(computer_card) < 17 and calculate_score(computer_card) != 0:
            sleep(0.5)
            card = deal_card()
            print(f"Computer's score less than 17, get another card: {card}")
            sleep(0.5)
            computer_card.append(card)
            print(f"Computer's cards: {computer_card} with {calculate_score(computer_card)} score")
            sleep(0.5)
        compare(calculate_score(user_card), calculate_score(computer_card))
    #Hint 14: Ask the user if they want to restart the game. If they answer yes,
    #clear the console and start a new game of blackjack and show the logo from art.py.
    conti = input("Do you want to play againt: ").lower()
    if conti == "y":
        restart()
        is_game_over = False
    else:
        is_game_over = True


print("Say Goodbye #")
