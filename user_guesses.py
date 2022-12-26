from random import randint
from math import log2, ceil

'''This Game needs User to suggest some range & then guess the randomely generated number'''
class User:
    '''This Class needs start & end values for range'''
    def __init__(self, start=0, end = 50):
        '''Storing range'''
        self.rangeN = (start, end)

        self.numGenerated = randint(start, end)
        
        '''Chances are calculated using the concept of binary search in which  the total iterations required to find a number would be atmost log2(total_array_size)'''
        self._setChances(ceil(log2(abs(self.rangeN[0] - self.rangeN[1]))))
        #print(self.numGenerated)
        
    def game(self, num):
        if num==self.numGenerated:
            return "Wow! You have won",'q'
        else:
            self._setChances(self._getChances() - 1)
            if self._getChances()==0:
                return "You have lost!!! The number is "+str(self.numGenerated),'q'
            if num > self.numGenerated:
                retStr = "LOWER"
            else:
                retStr = "HIGHER"
            return "You have to try again! Number is a bit "+retStr+" than what you have guessed & you have "+str(self._getChances())+" Chances left...", ''
    
    def _setChances(self, chances):
        self.chances = chances
    
    def _getChances(self):
        return self.chances

def userBegin():
    start, end = map(int, input("Enter the range starting & ending points: ").split())
    user = User(start, end)
    play = ''
    while play!='q':
        num = int(input("Guess the number: "))
        if num > end or num < start:
            print("You have guessed number out of selected range ({} - {}). Please Try again".format(start, end))
            continue
        play = user.game(num)
        print(play[0])
        play = play[1]

userBegin()
