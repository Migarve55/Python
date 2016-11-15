#
# Project from Miguel Garnacho Velez - Version BETA 2.2 - 12/11/2016
#
# To implement:
# - Use images for mines, flags, etc.
# - Replay button

from random import randint
from graphics import *

DEBUG = False #Use this to debug using the promt
CHEATS = True #Disable this if you want a fair game

INPUT = True #True to mouse, False to keyboard only

# Matrix of NxM size
true_board = []
player_board = []
sizeN = 16
sizeM = 16

# Graphics

screenSizeX = 400
screenSizeY = 400
window = GraphWin("Buscaminas", screenSizeX, screenSizeY)

cellSize = 20
gridXPos = 40
gridYPos = 30

#textGridX = gridXPos + (cellSize * sizeN) / 2
#textGridY = gridYPos + (cellSize * sizeM) / 2

textGridX = gridXPos + cellSize / 2
textGridY = gridYPos + cellSize / 2
textGridSize = 13

textX = screenSizeX / 2
textY = screenSizeY - 20

#List with the colors
toColor = ['green','blue','red','blue3','red3','cyan','black','gray']

# Chars for the board that the player sees
fllr = ' ' #Filler, when there is nothing in the board 
none = '.' #There is no mine here
expl = 'X' #Used when the player ticks a cell and is a mine
flag = 'P' #Flagged cell
crct = 'C' #Correct flagged cell, at he end of the game
erro = 'E' #Used when the player flagged a safe cell, showed at he end of the game
unkn = '?' #Used by the player to mark a suspicious cell
ufmn = 'Q' #This shows when the game end where is a mine that you did not flag (Un Flagged MiNe)

# Chars for the true board, which the game uses
noth = '.' #Nothing
mine = 'M' #Mine

player1_wins = 0
computer_wins = 0

game_running = True

#Variables used to change between modes
current_mode = False #Mouse mode
scan = False
mark = True
scanText = "Scanning"
markText = "Flagging"
keyChange = 'm'

def modeToText(m): #Converts the mode into text
    if m == scan:
        return scanText
    elif m == mark:
        return markText
    return None
    
def constrain(a, mn , mx): #Constrains a variable 'a' in a closed intereval [mn,mx]
    if a < mn:
        a = mn
    elif a > mx:
        a = mx
    return a

def create_true_board(sN, sM, mines): #Creates a board of NxM size with n mines, used by the game
    brd = []
    for i in range(sN):
        brd.append([noth] * sM)
    for m in range(mines):
        x = randint(0,sizeN - 1)
        y = randint(0,sizeM - 1)
        while brd[x][y] != noth:
            x = randint(0,sizeN - 1)
            y = randint(0,sizeM - 1)
        brd[x][y] = mine   
    return brd

def create_player_board(sN, sM): #Creates the board the player sees
    brd = []
    for i in range(sN):
        brd.append([fllr] * sM)
    return brd

def print_board(brd): #Prints the board in a readable form
    for item in brd:
        print(' '.join(item))

def player_input(): #Player input
    x = int(input("Enter X coordinates: "))
    y = int(input("Enter Y coordinates: "))
    while (x < 1 or x > sizeN) or (y < 1 or y > sizeN):
        x = int(input("Enter X coordinates: "))
        y = int(input("Enter Y coordinates: "))
    c = input("Select mode, leave it blank if you want(m,f): ").lower()
    if c == 'm':
        current_mode = mark
    elif c == 'f':
        current_mode = flag
    return x-1, y-1

def check_cell(x, y, tr_brd): #Checks a cell in [x,y] to display how many mines around, if any. Parameter "tr_brd" must be the true board
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            #print("Checking: [%i,%i]" % (constrain(x+i,0,sizeN-1),constrain(y+j,0,sizeM-1)))
            if (x+i >= 0 and x+i < sizeN) and (y+j >= 0 and y+j < sizeM):
                if tr_brd[x+i][y+j] == mine and not (i == 0 and j == 0):
                    count += 1
    if count != 0: #Stops
        player_board[x][y] = str(count)
    else: #Recursion
        player_board[x][y] = none
        for i in range(-1,2):
            for j in range(-1,2):
                if (x+i >= 0 and x+i < sizeN) and (y+j >= 0 and y+j < sizeM):
                    if not (i == 0 and j == 0) and player_board[x+i][y+j] in [fllr]:
                        check_cell(x+i,y+j, tr_brd)

def countLeftMines(total, ply_brd, tr_brd): #Counts mines
    count = 0
    for x in range(sizeN):
        for y in range(sizeM):
            if ply_brd[x][y] == flag:
                count += 1
    return constrain(total - count,0,total)

def gameEnded(ply_brd, tr_brd): #Displays where the mines were
    for x in range(sizeN):
        for y in range(sizeM):
            if ply_brd[x][y] in [fllr,unkn] and tr_brd[x][y] == mine:
                ply_brd[x][y] = ufmn
            if ply_brd[x][y] == flag: #When the player flagged a cell
                if tr_brd[x][y] == mine: #Correct
                    ply_brd[x][y] = crct
                else: #Error
                    ply_brd[x][y] = erro
    return ply_brd

def player_move(plyr_inp,tr_brd,ply_brd): #For every player move
    game_run = True
    x = plyr_inp[0]
    y = plyr_inp[1]
    if current_mode == scan: #Check for mines
        if tr_brd[x][y] == mine: #Game over
            ply_brd[x][y] = expl
            game_run = False
            print("Game over")
            ply_brd = gameEnded(ply_brd, tr_brd)#Shows where are the mines that you didn't spotted, and the wrong ones
        elif ply_brd[x][y] in [fllr,flag,unkn]: #Checks for mines around
            check_cell(x, y, tr_brd)
        else:
            pass
    elif current_mode == mark: #Marks cells
        if ply_brd[x][y] == fllr:
            ply_brd[x][y] = flag
        elif ply_brd[x][y] == flag:
            ply_brd[x][y] = unkn
        elif ply_brd[x][y] == unkn:
            ply_brd[x][y] = fllr
    else:
        print("Wrong player mouse input")
    return tr_brd, ply_brd, game_run #Returns the uploaded 

def win(tr_brd,ply_brd,mines): #This function returns if the players has won
    count = 0
    flags = 0
    for x in range(sizeN):
        for y in range(sizeM):
            if ply_brd[x][y] == flag and tr_brd[x][y] == mine:
                count += 1
    for x in range(sizeN):
        for y in range(sizeM):
            if ply_brd[x][y] == flag:
                flags += 1
    if mines == count and flags == count:
        return True
    return False

# ========================== GRAPHICS ============================ #

def mainDraw(txt, grpBrd, ply_brd, m):
    updateBoard(grpBrd, ply_brd)                                         #Updates the board
    txt.setText("Mines left: %i - Current mode: %s" % (countLeftMines(total_mines, ply_brd, true_board), modeToText(m))) #Updates text

def drawGrid(w, xPos, yPos, cellS, cellX, cellY):
    gridXSize = cellS * cellX 
    gridYSize = cellS * cellY
    #Border
    border = Rectangle(Point(xPos,yPos),Point(xPos+gridXSize,yPos+gridYSize))
    border.draw(w)
    #Grid
    for i in range(sizeN): #Columns
        line = Line(Point(xPos+i*cellS,yPos),Point(xPos+i*cellS,yPos+gridYSize))
        line.draw(w)
    for j in range(sizeM): #Columns
        line = Line(Point(xPos,yPos+j*cellS),Point(xPos+gridXSize,yPos+j*cellS))
        line.draw(w)


def drawPlayerBoard(w, xPos, yPos, cellS, cellX, cellY, textSize, ply_brd): #Creates the player board
    graphBoard = []
    row = []
    for y in range(cellY):
        for x in range(cellX):
            row.append(Text(Point(xPos+(x*cellS),yPos+(y*cellS)),fllr))
            row[x].setSize(textSize)
            row[x].draw(w)
        graphBoard.append(row)
        row = []
    return graphBoard

def updateBoard(grpBrd, ply_brd): #Updates it
    for x in range(len(ply_brd)):
        for y in range(len(ply_brd[0])):
            char = str(ply_brd[x][y])
            if char.isdigit(): #Is a number
                grpBrd[x][y].setText(char)
                grpBrd[x][y].setTextColor(toColor[int(char)-1])
            else:
                grpBrd[x][y].setTextColor("black")
                grpBrd[x][y].setText(char)

def drawText(w, xPos, yPos, mines):
    text = Text(Point(xPos,yPos), 'nothing')
    text.setText("Mines left: %i - Current mode: %s" % (countLeftMines(total_mines, player_board, true_board), modeToText(current_mode)))
    text.draw(w)
    return text

def mouse_input(w, xPos, yPos, cellS, cellX, cellY):
    point = w.checkMouse()
    if DEBUG and point != None:
        print("Raw mouse:" + str(point))
    gridXSize = cellS * (cellX+2) 
    gridYSize = cellS * (cellY+2)
    if point == None:
        return 'null'
    if (point.x >= xPos and point.x <= gridXSize) and (point.y >= yPos and point.y <= gridYSize): #Over the grid
        X = int((point.x-xPos) / cellS)
        Y = int((point.y-yPos) / cellS)
        return Y, X
    return 'null'

def changeMode(w, t, m):
    inp = w.checkKey().lower()
    if inp == keyChange:
        m = not m
    if DEBUG and inp != '':
        print("Key: " + str(inp))
        print(modeToText(current_mode))
    t.setText("Mines left: %i - Current mode: %s" % (countLeftMines(total_mines, player_board, true_board), modeToText(m))) #Updates text
    return m

def selDif():
    inp = int(input("Select the diffilculty (1,2,3...): "))
    while inp < 1:
        inp = int(input("Select the diffilculty (1,2,3...): "))
    return abs(inp * 5)

#Init

percentage = selDif()
total_mines = int(sizeN * sizeM * percentage / 100)

true_board = create_true_board(sizeN, sizeM, total_mines)
player_board = create_player_board(sizeN, sizeM)

if CHEATS:
    print("True board:")
    print_board(true_board)

if not INPUT:
    print("Player board:")
    print_board(player_board)
else:
    print("Use the key '%c' to change between modes" % (keyChange))

drawGrid(window,gridXPos,gridYPos,cellSize,sizeN,sizeM) #Draws the grid
text = drawText(window, textX, textY, total_mines) #Creates the text object
graphBoard = drawPlayerBoard(window,textGridX,textGridY,cellSize,sizeN,sizeM,textGridSize,player_board)


# ============================= GAME ============================= #

print("Game started")

while game_running:
    if INPUT:
        inp = mouse_input(window,gridXPos,gridYPos,cellSize,sizeN,sizeM)
        current_mode = changeMode(window, text, current_mode)
        while inp == 'null':
            inp = mouse_input(window,gridXPos,gridYPos,cellSize,sizeN,sizeM)
            current_mode = changeMode(window, text, current_mode)
        if DEBUG:
            print(inp)
    else:
        inp = player_input()
        print("Player board: %i Mines left" % (countLeftMines(total_mines, player_board, true_board)))
        print_board(player_board)
    result = player_move(inp,true_board,player_board)
    true_board = result[0]
    player_board = result[1]
    game_running = result[2]
    if win(true_board,player_board,total_mines):
        player_board = gameEnded(player_board, true_board)
        print("You won! Congratulations!")
        game_running = False
    mainDraw(text, graphBoard, player_board, current_mode)

print("Game ended")
#Waits for key input to close
window.getKey()
window.close()
