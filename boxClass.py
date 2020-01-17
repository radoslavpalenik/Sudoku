import mapGenerator

class Box():
    '''
    Smallest unit of game field.
    '''

    def __init__(self, val):
        '''
        initialize box variables
        '''
        #if value is seted by default, box will be locked, beacause user can't set another, than default value
        self.lock = False
        self.value = val

    def setValue(self, value):
        '''
        value insertion
        '''
        if ((value in range(0,9)) and (not self.lock)):
            self.configure(text = value)


    def setTip(self, tip):
        '''
        add tip into list
        '''
        if (not self.lock):
            self.tip.add(tip)


    def removeTip(self, tip):
        '''
        remove tip from list
        '''
        self.tip.remove(tip)


    def isLocked(self):
        '''
        Return lock value
        '''
        return self.lock
