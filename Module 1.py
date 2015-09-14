
from random import randint
player1 = input("What is your name?")



class Die(object):
    def __init__(self, sides=6, number=None):
        self.sides = sides
        self.number = number

    def roll(self):
        self.number = randint(1, self.sides)
        return self.number

d1 = Die()
d2 = Die()

class ScoreCard(object):
    def __init__(self, amount = 0):
        self.amount = amount

    def add(self, points):
        self.amount = self.amount + points
        return self.amount

    def current_score(self):
        return self.amount

    def current_score_print(self):
        print("Your score is: " + str(self.amount))

player1score= ScoreCard()


def choice():
    while player1score.current_score() < 22:
        if player1score.current_score() == 21:
            break
        else:
            choice=int(input("How many dice would you like to roll again?"))
            if choice == 1:
                d1.roll()
                player1score.add(d1.number)
                print ("You rolled a " + str(d1.number))
                player1score.current_score_print()

            elif choice == 2:
                d1.roll()
                d2.roll()
                player1score.add(d1.number)
                player1score.add(d2.number)
                print ("You rolled a " + str(d1.number) + " and a "\
                   + str(d2.number))
                player1score.current_score_print()
            else :
                print("Please only enter 1 or 2. Try agian:")


    if player1score.current_score() == 21:
        print ("You've won!")
    else:
        print ("You've gone over!")

def play_game():
    print ("Welcome to Black Jack Dice, " + player1 + "! The rules are simple: You start with" \
          " two randomly thrown dice ")
    print ("and your starting score is the value of the dice. You can choose to roll one or both")
    print ("of the dice to get more points. The goal is to get to 21 with out going over.")

    d1.roll()
    player1score.add(d1.number)
    d2.roll()
    player1score.add(d2.number)
    print ("You rolled a " + str(d1.number) + " and a "\
           + str(d2.number))
    player1score.current_score_print()
    choice()

play_game()


