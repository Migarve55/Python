#Lesson 2 exercises

import math 

def solveEq(a,b,c):
    if (a == 0):
        print("Its no second grade")
    elif(b**2 - 4*a*c < 0):
        print("There is no solution")
    elif(b**2 - 4*a*c == 0):
        print("There is only one solution: %f" % ((-b + math.sqrt(b**2 - 4*a*c))/(2*a)))
    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        print("Solution: %f , %f" % (x1,x2))

def fantasyGame(): #6
    print("Welcome to Ever's Quest")
    name = input("Enter the name of your character: ")
    strength = int(input("Enter the strenght of your character: "))
    health = int(input("Enter the health of your character: "))
    luck = int(input("Enter the luck of your character: "))
    if (strength+health+luck>15):
        strength = 5
        health = 5
        luck = 5
        print("You have give your character too many points! Default values have been assigned: Chortle, strength: 5, health: 5, luck: 5")

def FizzBuzz(): #7
    for n in range(1,101):
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif (n % 3 == 0):
            print("Fizz")
        elif (n % 5 == 0):
            print("Buzz")
        else:
            print(n)

#8 its the second one a=20 b=20

def negative(n):#9
    if n < 0:
        print("negative")
    pass

def youngest():#10
    a = input("A: ")
    b = input("B: ")
    print(min(a,b))

def ex11():
    a = input("A: ")
    if (a == '('):
        print("Its ( boi")

def ex12():
    a = input("A: ")
    if (a.isupper()):
        print("It’s uppercase")
    
#fantasyGame()
#FizzBuzz()
