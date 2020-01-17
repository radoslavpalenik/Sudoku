import random
import mapGenerator
import boxClass
def generateMap(index):
    count = 0;

    def generateValue(index):
        return random.randint(1,9)

class Sudoku():
    '''
    3x3 block of boxes
    '''
    gameBoard = 0
    box = [[0 for x in range(9)] for y in range(9)]
    def init(self, Level):
        '''
        init block contains 9 boxes
        '''
        self.gameBoard = mapGenerator.generateGameBoard(Level)
        for x in range(0,9):
                for y in range (0,9):
                    self.box[x][y] = boxClass.Box(self.gameBoard[x][y])

    def reset(self, Level): 
        self.gameBoard = mapGenerator.generateGameBoard(Level)
        for x in range(0,9):
            for y in range (0,9):
                self.box[x][y] = boxClass.Box(self.gameBoard[x][y])

    def checkMissing(self,number):
        numberCount = 0
        for x in range(0,9):
            for y in range (0,9):
                if (number == self.gameBoard[x][y]):
                    numberCount += 1
        return (9 - numberCount)