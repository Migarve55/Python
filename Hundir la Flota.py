from random import randint

board = []
ships = []

size = max(int(input("Size of the battleground: ")),15)
shipPer = max(int(input("Percent of battleships(%): ")),100)
shipsSize = max(int(input("Size of the battleships: ")),size)
shipsNumber = int(((size ** 2) * (shipPer / 100)) / shipsSize) 
turns = int(input("Turns: ")) 
shipsSinked = 0

if shipsSize * shipsNumber > size ** 2:
    print("Error: there is not enought space") 
    exit()

if shipsNumber > turns:
    print("This is impossible, mate!")
    turns = shipsNumber + 15
    print("Now your turns are: ", turns)

# Crea el tablero

for x in range(size):
    board.append(["O"] * size)
    
for x in range(size):
    ships.append(['W'] * size)

def print_board(board):
    for row in board:
        print("  ".join(row))

def print_ships(ships):
    for row in ships:
        print("  ".join(row))

print("Let's play Battleship!")
print_board(board)

#Functions 

def newShip(board):    
    while True:        
        shipRow = randint(0, len(board) - 1)    #Row
        shipCol = randint(0, len(board[0]) - 1) #Col
        if ships[shipRow][shipCol] != 'S':
            ships[shipRow][shipCol] = 'S'
            break

def newBigShip(board, ship_size, pos):

    if pos == 'horizontal':
        while True:
            shipRow = randint(0, len(board) - 1)    #Row
            shipCol = randint(0, len(board[0]) - 1) #Col
            for x in range(shipCol,ship_size): #Comprueba si todo esta correcto
                if ships[x][shipCol] == 'S':
                    break
            else:    
                for x in range(shipCol,ship_size): # Los crea
                    ships[x][shipCol] = 'S'
                    break
    elif pos == 'vertical':
        print("Can't do right now")
        print_ships(ships)#Solo debug
    
  
for i in range(shipsNumber):
    newShip(board)
    #newBigShip(board, shipsSize, 'horizontal')

print_ships(ships) #Solo para debug        

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!

for turn in range(turns):

    guess_row = int(input("Guess Row:")) 
    guess_col = int(input("Guess Col:"))

    if (guess_row < 0 or guess_row > size - 1) or (guess_col < 0 or guess_col > size - 1):
        print("Oops, that's not even in the ocean.")
        guess_row = 0
        guess_col = 0

    if ships[guess_row][guess_col] == 'S':
            if board[guess_row][guess_col] == "S":
                print("You have already sinked that battleship")
            else:
                print("You sunk my battleship!")
                if shipsSinked == shipsNumber:
                    print("Congratulations! You sunk all my battleships!")
                else:
                    board[guess_row][guess_col] = "S"
                    shipsSinked += 1
    else:
        if board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    if turn == turns - 1:
        print("Game Over")
    # Print (turn + 1) here!
    print("Turn: {} / {}".format(turn, turns))
    print("Ships: {} / {}".format(shipsNumber - shipsSinked,shipsNumber))
    print_board(board)
    
print_ships(ships)
