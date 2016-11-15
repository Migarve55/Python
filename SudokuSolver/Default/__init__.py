'''
Created on 8 oct. 2016
Last modification: 10 oct. 2016

@author: migarve55
'''

import random
from SudokuCreator import attempt_board as ab
import itertools
from pip._vendor.distlib.compat import raw_input
import time

print("Sudoku solver V-1.1.2 10/10/2016")

size = 9

sudoku = []
sudokuMarkers = []
LOOP = True
MAX_LOOPS = 16

DEBUG = True
solved = 0

#We create a 9x9 matrix

sudoku = [[0 for _ in range(size)] for _ in range(size)]

#We create a 9x9 matrix

sudokuMarkers = [[None for _ in range(size)] for _ in range(size)]

sudoku = [[8,2,3,4,0,6,0,0,0],
          [1,4,5,0,0,0,0,0,0],
          [0,7,6,0,0,0,9,0,0],
          [0,0,0,0,0,0,0,0,7],
          [7,0,0,0,5,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,5,4,0,0,0,0,0,0],
          [0,6,7,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1]]

def markCell(row,col,sdk):
    result = []
    #Check horizontal
    horRow = sdk[row]
    #Check vertical
    verRow = []
    for n in range(len(sdk[col])):
        verRow.append(sdk[n][col])
    #Check cell
    cell = []
    n = lambda x: (int(x / 3) + 1) * 3 - 3
    initX = n(row)
    initY = n(col)
    for i in range(initX,initX + 3):
        for j in range(initY,initY + 3):
            cell.append(sdk[i][j])

    #Check if you can mark
    for num in range(1,10): #For each number 1-9
        if(num not in horRow and num not in verRow and num not in cell) and sdk[row][col] == 0:
            result.append(num)
    return result

#We set up the markers function
def setMarkers(sdk):
    sdkMarkers = []
    for n in range(size):
        sdkMarkers.append([[]] * size)

    for i in range(size):
        for j in range(size):
            sdkMarkers[i][j].append(markCell(i,j,sdk))

    return sdkMarkers

def fillSdk(sdk, sdkMrk): #Solve it
    #Horizontal prop
    for i, j in itertools.product(range(size), repeat=2):
        if DEBUG and not len(sdkMrk[i][0][j]) == 0:
            sdm=sdkMrk[i][0][j]
        if(len(sdkMrk[i][0][j]) == 1 and sdk[i][j] == 0):
            sdk[i][j] = sdkMrk[i][0][j][0]
            if DEBUG:
                print(str(sdm)+"Pos: %i,%i set to: %i" % (i,j,sdkMrk[i][0][j][0]))
    return sdk

def is_full(sdk): #Check if it is full
    for item in sdk:
        for c in item:
            if c == 0:
                return False
    return True

def printPrettySdk(sdk): #Print in the console so it is easy to read
    line = ""
    for i in range(len(sdk)):
        for j in range(len(sdk[i])):
            line += " " + str(sdk[i][j])
            if (j in [2,5]):
                line += " |"
        print(line)
        line = ""
        if (i in [2,5]):
            print("-" * 22)

def printMarkers(mrk):
    for i in range(len(mrk)):
        for j in range(len(mrk[0])):
            if not mrk[i][0][j] == []:
                print(("Cell row:%i col:%i: " % (i+1,j+1)) + str(mrk[i][0][j]))

def generateSudoku(s,sc):#Generates a random sudoku
    sudoku = ab(s,sc)
    while (sudoku == None):
        sudoku = ab(s,sc)
    return sudoku

#Filler test

#sudokuMarkers = setMarkers(sudoku)
#sudoku = fillSdk(sudoku, sudokuMarkers)
#printPrettySdk(sudoku)

#Main loop

def solve_sudoku(sudoku,loop):
    #print("Starting solving the sudoku: ")
    loops = 1
    oldS = []
    while(loop): #Main loop
        if DEBUG:
            print("Loop: " + str(loops))
        #We start setting the markers
        sudokuMarkers = setMarkers(sudoku)
        #We fill the gaps where there is only one posible solution
        sudoku = fillSdk(sudoku, sudokuMarkers)
        #We check its completed
        if sudoku == oldS or loops > MAX_LOOPS or is_full(sudoku):
            loop = False
            if is_full(sudoku):
                print("Finished within this loops: " + str(loops))
                #solved += 1
            elif loops > MAX_LOOPS:
                print("Out of loops")
            elif DEBUG:
                print("The algorithm got stuck in loop: " + str(loops))
                printMarkers(setMarkers(sudoku))
            else:
                print("Could not finish, use debug for more info")
        loops += 1
        #oldS = sudoku

    return sudoku


#Testing units

#Test

n_tests = int(raw_input("Number of tests per number of initial cells: "))
n_init = int(raw_input("Initial number of cells: "))
n_end = int(raw_input("Final number of tests: "))

start_time = time.time()

for cells in range(n_init,n_end+1):
    print("------Initial cells: " + str(cells) + "------")
    for n in range(n_tests):
        print("---Test: " + str(n+1) + "---")
        s = generateSudoku(3,cells)
        if DEBUG:
            printPrettySdk(s)
        solved = solve_sudoku(s,LOOP)
        if DEBUG:
            printPrettySdk(solved)

run_time = time.time() - start_time
n_total_tests = n_tests * (n_end - n_init)
average = run_time / n_total_tests

print("--- Runtime: %s seconds solving %i sudokus | Average time: %f---" % (run_time, n_total_tests, average))




