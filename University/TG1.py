#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      UO257431
#
# Created:     17/11/2016
# Copyright:   (c) UO257431 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def userInput():
    inp = raw_input("Continuar? (Si/No): ").lower()
    while inp not in ['si','no']:
        inp = raw_input("Continuar? (Si/No): ").lower()
    if inp == 'si':
        return True
    elif inp == 'no':
        return False

def ex1():
    line = ''
    col = 0
    Continue = True
    for n in range(100, 501):
        if n % 6 == 0:
            line += str(n) + ' '
            col += 1
        if (col == 5):
            col = 0
            print(line)
            line = ''
            if not userInput():
                break

def ex2():
    pages = 400
    alberto = 0
    maria = 0
    mP = 15
    day = 0
    while maria < pages and alberto < pages:
        day += 1
        alberto += 45
        maria += mP
        mP += 10
        print("Day %i: Maria: %i Alberto %i" % (day,maria,alberto))
    if maria > alberto:
        print("Maria finished first")
    elif alberto > maria:
        print("Alberto finished first")
    else:
        print("They finished at the same time")

def main():
    ex1()
    #ex2()


if __name__ == '__main__':
    main()
