'''
Created on 9 oct. 2016
Last modification: 9 oct. 2016

@author: migarve55
@note: Used with sudoku solver together, modified from stack overflow
'''

import itertools
import random

def attempt_board(m=3,c=0):
    """Make one attempt to generate a filled m**2 x m**2 Sudoku board,
    returning the board if successful, or None if not.

    """
    n = m**2
    c = n**2 - c

    numbers = list(range(1, n + 1))
    board = [[None for _ in range(n)] for _ in range(n)]
    for i, j in itertools.product(range(n), repeat=2):
        i0, j0 = i - i % m, j - j % m # origin of mxm block
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])):
                board[i][j] = x
                break
        else:
            # No number is valid in this cell.
            return None
    for num in range(c): #Put blank spaces c times
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        board[i][j] = 0
    return board
