
def putValue( x, y, val, cont):
    print("changing value ["+str(x)+"]["+str(y)+"]")
    sdkBtn[x][y].configure(text = str(val))
    sudoku.gameBoard[x][y] = val

    isMatrixCorrect = mapGenerator.checkIfSolved(sudoku.gameBoard)

    if(isMatrixCorrect):
        print("vyriesene")
        cont.show_frame(SummaryScreen, False)
    else:
        print("nevyriesene")
    self.update()

class Controller():

    def __init__(self):
        
