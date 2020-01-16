# sudoku generator implementation
# this source is taken from https://codereview.stackexchange.com/questions/88849/sudoku-puzzle-generator
# author: Gareth Rees

import random

def make_board(m=3):
    """Return a random filled m**2 x m**2 Sudoku board."""
    n = m**2
    board = [[0 for x in range(9)] for y in range(9)]

    def search(c=0):
        "Recursively search for a solution starting at position c."
        i, j = divmod(c, n)
        i0, j0 = i - i % m, j - j % m # Origin of mxm block
        numbers = list(range(1, n + 1))
        random.shuffle(numbers)
        for x in numbers:
            if (x not in board[i]                     # row
                and all(row[j] != x for row in board) # column
                and all(x not in row[j0:j0+m]         # block
                        for row in board[i0:i])): 
                board[i][j] = x
                if c + 1 >= n**2 or search(c + 1):
                    return board
        else:
            # No number is valid in this cell: backtrack and try again.
            board[i][j] = None
            return None

    return search()


def generateMask():
    mask = [[0 for x in range(9)] for y in range(9)]
    maskTemplate = [0,0,0,0,0,0,1,0,0]
    for x in range(0,9):
        random.shuffle(maskTemplate)
        for y in range (0,9):  
            mask[x][y] = maskTemplate[y]

    return mask

def generateGameBoard():
    gameBoard = [[0 for x in range(9)] for y in range(9)]
    global solvedBoard
    solvedBoard = make_board(3)

    print("----------------------------------")
    for x in range(0,9):
            print(str(solvedBoard[x][0])+str(solvedBoard[x][1])+str(solvedBoard[x][2])+str(solvedBoard[x][3])+str(solvedBoard[x][4])+str(solvedBoard[x][5])+str(solvedBoard[x][6])+str(solvedBoard[x][7])+str(solvedBoard[x][8]))
 

    
    mask = generateMask()
    for x in range(0,9):
        for y in range (0,9):
            if(mask[x][y] == 0):
                gameBoard[x][y] = solvedBoard[x][y]
            else:
                gameBoard[x][y] = None

    print("----------------------------------")
    for x in range(0,9):
            print(str(gameBoard[x][0])+str(gameBoard[x][1])+str(gameBoard[x][2])+str(gameBoard[x][3])+str(gameBoard[x][4])+str(gameBoard[x][5])+str(gameBoard[x][6])+str(gameBoard[x][7])+str(gameBoard[x][8]))
 
    
    
    
    return gameBoard

def checkIfSolved(gameBoard):
    solved = False
    for x in range(0,9):
        for y in range (0,9):
            if(gameBoard == solvedBoard):
                solved = True
            else:
                solved = False
    return solved


    



            


