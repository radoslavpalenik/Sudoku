#!/usr/bin/env python3

import random

def generateMap(index):
    count = 0;

    def generateValue(index):
        return random.randint(1,9)

class Sudoku():
    '''
    3x3 block of boxes
    '''

    def __init__(self):
        '''
        init block contains 9 boxes
        '''
        self.boxes[i][j] = Box(generateMap(i));


