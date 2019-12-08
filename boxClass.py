class Box():
    '''
    Smallest unit of game field.
    '''

    def __init__(self, val):
        '''
        initialize box variables
        '''

        #if value is seted by default, box will be locked, beacause user can't set another, than default value
        if (value in range(1,9)):
            self.lock = True
            self.value = val
        else:
            self.lock = False
            self.value = 0  #value insade box

        self.tip = set()   #list, which will contain hint by user


    def setValue(self, value):
        '''
        value insertion
        '''
        if ((value in range(0,9)) and (not self.lock)):
            self.value = value


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


    def isLocked(self)
        '''
        Return lock value
        '''
        return self.lock
