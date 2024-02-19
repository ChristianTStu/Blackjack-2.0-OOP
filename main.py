from card import Card
from hand import Hand
import random
import os


# Default options
shuffle_count = 100000
deck_size = 8
player_count = 2        # we will assume that player 0 is the dealer
hands = []
wins = 0
games = 0

deck = []
suits = ["S","C","H","D"]
faces = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
values = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def createDeck():
    for d in range(1, deck_size):
        for s in suits:
            for i in range(12):
                is_ace = False
                if values[i] == 11:
                    is_ace = True
                card = Card(s, faces[i], values[i], is_ace)
                deck.append(card)


def shuffle(deck):
    # Note: Python has a random.shuffle() function that
    #       could also be used, however there is much
    #       less control over iterations

    global shuffle_count

    for i in range(shuffle_count):
        x = random.randint(0, len(deck)-1)
        y = random.randint(0, len(deck)-1)

        temp = deck[x]
        deck[x] = deck[y]
        deck[y] = temp


def playHand():

    hands.clear()
    os.system('cls||clear')

    # create the player hands
    for p in range(player_count + 1):
        hand = Hand()
        hands.append(hand)

    # go around the table
    for i in range(2):
        for h in hands:
            h.addCard(deck[0])
            deck.pop(0)

    print("Your hand is", hands[1].printHand(), "for a value of", hands[1].getHandValue())
    print("The revealed dealer card is", hands[0].cards[1].value)

    play = input("Would you like to [h]it or [s]tand? ")

    while play == "h" and hands[1].getHandValue() <= 21:
        hands[1].addCard(deck[0])
        deck.pop(0)

        if hands[1].getHandValue() < 21:
            print("Your hand is", hands[1].printHand(), "for a value of", hands[1].getHandValue())
            print("The revealed dealer card is", hands[0].cards[1].value)

            play = input("Would you like to [h]it or [s]tand? ")

        elif hands[1].getHandValue() == 21:
            print("You have 21!")
        else:
            print("You've bust, loser...")
            break

    print("The dealer has ", hands[0].printHand(), "for a value of", hands[0].getHandValue())

    while hands[0].getHandValue() <17:
        hands[0].addCard(deck[0])
        deck.pop(0)
    
    print("The final dealer hands is", hands[0].printHand(), "for a value of", hands[0].getHandValue())

    if hands[0].getHandValue() <=21 and hands[1].getHandValue() <=21:
        if hands[0].getHandValue() > hands[1].getHandValue():
            print("You lose, loser...")
        elif hands[0].getHandValue() == hands[1].getHandValue():
            print("Ugh, a draw")
        else:
            print("Wow, you actually won?")
            global wins
            wins += 1
    elif hands[0].getHandValue() > 21 and hands[1].getHandValue() <=21:
        print("The dealer is a loser")

    global games
    games += 1
    

createDeck()
shuffle(deck)

gameon = "y"

while gameon == "y":
    os.system('cls||clear')
    playHand()

    print("You have played", games, "games and won", wins, "of them")

    gameon = input("New hand? [y|n]")