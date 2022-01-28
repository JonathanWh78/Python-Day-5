# Dice Class
# - Write a class called Dice
# - When initialised the object will set how many faces the die has
# - Create objects for 6, 20, 2 and 4 sided die.
# - Roll a charactor sheet for a Swashbuckler Rogue called 'Earl Grey' DnD 5th ed.

from pydoc import describe
from random import randint

#class for setting default face to 6 and has a roll function
class Dice:
    def __init__(self, NoofFaces = 6):
        self.NoofFaces = NoofFaces

    def Roll(Die):
        rdmroll = randint (1, Die)
        return rdmroll

    # def quantity(number, DSelect):
    #     if DSelect == 2:
    #         for i in range(number):
    #             print("Result: You Rolled a D4 And Got A: " +str(Dice.Roll(D4.NoofFaces)))


#objects overwite the default value with the correct one for the dice
D2 = Dice(2)
D4 = Dice(4)

#Loop to make it feel more interactive
DSelect = int
while DSelect != 0:
    print("")
    print("-----------------------")
    print("Press 1: To Flip A Coin")
    print("Press 2: To Roll A D4")
    print("Press 0: To Quit")
    print("-----------------------")
    print("")
    DSelect = int(input("Please Select An Option: "))
    print("")
    if DSelect == 1:
        Roll = Dice.Roll(D2.NoofFaces)
        if Roll == 1:
            print("------------------------------------------")
            print ("Result: You Flipped A Coin And Got: Heads")
            print("------------------------------------------")
        elif Roll == 2:
            print("------------------------------------------")
            print ("Result: You Flipped A Coin And Got: Tails")
            print("------------------------------------------")
    elif DSelect == 2:
        quantity = int(input ("how many: "))
        for i in range(quantity):
                Roll = Dice.Roll(D4.NoofFaces)
                print("----------------------------------------------")
                print("Result: You Rolled a D4 And Got A: " +str(Roll))
                print("----------------------------------------------")

    elif DSelect == 0:
        print("-------------------")
        print ("Thanks For Playing")
        print("-------------------")
        print("")
    else:
        print("------------------------------------------")
        print ("Please Enter One Of The Specified Options")
        print("------------------------------------------")