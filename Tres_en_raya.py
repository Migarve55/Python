from random import randint

board = []
size = 3
filler = '-'

player1_wins = 0
player2_wins = 0

for i in range(size):
    board.append([filler] * size)

def reboot():
    for item in board:
        for i in range(len(item)):
            item[i] = filler
    print("Your wins: %i - Computer's wins: %i" % (player1_wins,player2_wins))

def print_board(brd):
    for item in brd:
        print(' '.join(item))

def check_for_row(row, char):
    for i in range(len(row)):
        if row[i] == char:
            return i
    return 0

def check_for_col(col, char):
    for i in range(len(board[0])):
        if board[i][col] == char:
            return i
    return 0

def check(char):

    vert = ''
    #Mira las horinzontales
    for item in board:
        if ''.join(item) == char * size:
            return True

    #Mira las verticales
    for i in range(size):
        for item in board:
            vert += item[i - 1]
        if vert == char * size:
            return True
        vert = ''

    #Mira las diagonales
    for i in range(size):
        vert += board[i - 1][i - 1]
    if vert == char * 3:
        return True
    vert = ''
    for i in range(size):
        vert += board[i][2 - i]
    if vert == char * 3:
        return True

def about_to_win(brd, char):
    lenght = len(brd) - 1
    check = 0
    result = []
    for i in range(len(brd)): #Hor
        for j in range(len(brd[i])):
            if brd[i][j] == char:
                check += 1
        if check == lenght:
            j = check_for_row(brd[i],filler)
            result.append([[j],[i]]) # X, Y
        check = 0
    for i in range(len(brd)): #Ver
        for j in range(len(brd[i])):
            if brd[j][i] == char:
                check += 1
        if check == lenght:
            j = check_for_col(i,filler)
            result.append([[i],[j]]) # X, Y
        check = 0
    #Diagonal \
    for i in range(len(brd)):
        if brd[i][i] == char:
            check += 1
    if check == lenght:
        for i in range(len(brd)):
            if brd[i][i] == filler:
                result.append([[i],[i]])
    check = 0
    #Diagonal /
    for i in range(len(brd)):
        if brd[i][len(brd) - 1 - i] == char:
            check += 1

    if check == lenght:
        for i in range(len(brd)):
            if brd[i][len(brd) - 1 - i] == filler:
                result.append([[len(brd) - 1 - i],[i]])
    return result

def is_full(brd):
    for item in brd:
        for c in item:
            if c == filler:
                return False
    return True

print_board(board)

def player_1(x, y):
    if (x < 1 or x > size) or (y < 1 or y > size):
        x = 1
        y = 1
    if board[y - 1][x - 1] == 'O':
        print("You can't write over the others player's movements")
    elif board[y - 1][x - 1] != 'X':
        board[y - 1][x - 1] = 'X'
    else:
        print("You already input that")

def player_2():

    #Comprueba si estas a punto de ganar
    estatus = about_to_win(board,'X')
    to_win = about_to_win(board,'O')
    safe = True
    moved = False

    if to_win != []: #Para ganar
        for pos in to_win:
            x = int(pos[0][0])
            y = int(pos[1][0])
            if board[y][x] == filler:
                board[y][x] = 'O'
                moved = True
                break

    if estatus != [] and not moved: #Defensa
        for pos in estatus:
            x = int(pos[0][0])
            y = int(pos[1][0])
            if board[y][x] == filler:
                board[y][x] = 'O'
                moved = True
                break

    if not moved: #No ha podido escribir nada

        if True: #Aleatorio
            #print("Random")
            x = randint(0,len(board) - 1)
            y = randint(0,len(board[0]) - 1)
            while (board[y][x] != filler):
                x = randint(0,len(board) - 1)
                y = randint(0,len(board[0]) - 1)
                if is_full(board):
                    break
            if board[y][x] == filler:
                board[y][x] = 'O'

while True: #Main loop

    print("Your turn: ")
    player_1(int(input("Enter X: ")),int(input("Enter Y: ")))
    print_board(board)
    if check('X'):
        print("You win!")
        player1_wins += 1
        reboot();

    print("Computer's turn:")
    player_2()
    print_board(board)
    if check('O'):
        print("You loose!")
        player2_wins += 1
        reboot();

    if is_full(board):
        print("Board is full. Rebooting.")
        reboot();






