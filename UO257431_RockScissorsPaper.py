#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO257431
#
# Created:     14/10/2016
# Copyright:   (c) UO257431 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def UserInput():
    inp = raw_input("rock, paper, scissors (Q to quit)?: ").upper() #Register user input
    while inp not in ['R','P','S','Q']: #Check the sintax
        inp = raw_input("rock, paper, scissors (Q to quit)?: ").upper() #Register user input
        print("Im sorry, I only understand r, p, s")
    return inp

def main():
    name = raw_input("What is your name?: ") #Ask for your name
    print("Hello, " + name)

    LOOP = True
    userWins = 0
    computerWins = 0

    moves = ['R','P','S']

    while LOOP:
        userInput = UserInput()
        if userInput == 'Q': #Quit game
            LOOP = False
            break
        else: #Player movements
            computerMove = moves[random.randrange(3)] #Computer move

            if userInput == 'R':
                if computerMove == 'R':
                    print(name + " says rock, computer says rock: Draw!")
                if computerMove == 'P':
                    print(name + " says rock, computer says paper: computer wins!!")
                    computerWins += 1
                if computerMove == 'S':
                    print(name + " says rock, computer says scissor: " + name + " wins!")
                    userWins += 1

            elif userInput == 'P':
                if computerMove == 'R':
                    print(name + " says paper, computer says rock: " + name + " wins!")
                    userWins += 1
                if computerMove == 'P':
                    print(name + " says paper, computer says paper: Draw!")
                if computerMove == 'S':
                    print(name + " says paper, computer says scissor: computer wins!!")
                    computerWins += 1

            elif userInput == 'S':
                if computerMove == 'R':
                    print(name + " says scissor, computer says rock: computer wins!!")
                    computerWins += 1
                if computerMove == 'P':
                    print(name + " says scissor, computer says paper: " + name + " wins!")
                    userWins += 1
                if computerMove == 'S':
                    print(name + " says scissor, computer says scissor: Draw!")

        if userWins == 3 or computerWins == 3:
            LOOP = False
            break
        print("%i - %i" % (userWins, computerWins)) #Print scores

    if computerWins == userWins: #Draw
        print("We draw!")
    elif computerWins < userWins:
        print("You win!")
    elif computerWins > userWins:
        print("You lose!")
    print("Thank you for playing, " + name)

if __name__ == '__main__':
    main()
