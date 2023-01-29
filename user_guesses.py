from random import randint
from math import log2, ceil

'''This Game needs User to suggest some range to genarate a random number which the user has to guess in given number of chances'''
class User:
    '''This Class takes start & end values for range on initialization of object'''
    def __init__(self, start: int, end: int):
        ''' Storing range in variable: rangeN in tuple'''
        self.rangeN = (start, end)

        ''' Variable: NumGenerated generates the random number using randint method from random module which returns random integer in range, including both end points.'''
        self.numGenerated = randint(start, end)
        
        ''' Chances are calculated using the concept of binary search in which the total iterations required to find a number would be atmost log2(total_array_size)
        # self._setChances(ceil(log2(abs(start - end))))'''
        self._setChances(ceil(log2(abs(self.rangeN[0] - self.rangeN[1]))))
    
        #print(self.numGenerated)   # for check

    
    def game(self, num: int) -> tuple:
        '''The "game" Method takes num which is entered by the user/player & returns a tuple of strings'''  
        if self.numGenerated == num:
            return "Wow! You have won", False
            '''On this, Current game will end'''
        else:
            self._setChances(self._getChances() - 1)
            '''Here, 1 Chance has been used, so have to decrease it by 1 & update the chances by calling setChances method by getting the chances from getChances methods'''

            if self._getChances()==0:
                '''This will check if the last chance was used, so the user has lost the game & the current game will end here'''
                return "You have lost!!! The number is "+str(self.numGenerated), False

            if num > self.numGenerated:
                retStr = "LOWER"
                '''this condition is checking if number guessed is lower than the generated one'''
            else:
                retStr = "HIGHER"
                '''this condition is checking if number guessed is higher than the generated one'''
            return "You have to try again! Number is a bit "+retStr+" than what you have guessed & you have "+str(self._getChances())+" Chances left...", True
    
    def _setChances(self, chances: int) -> None:
        '''This method takes & sets chances for the user'''
        self.chances = chances
    
    def _getChances(self) -> int:
        'This method returns number of chances'
        return self.chances

def userBegin():
    '''This function is where User begins the game.
    It asks user the start & end points of the range & creates a new object for the user'''
    '''This "play" flag is False initially Because we are treating the user has not entered the correct datatype for start & end points'''
    play = False
    
    while play == False:
        try:
            '''This try-except block is to check if user is only entring numbers & not any data type.'''
            start = int(input("Enter the range starting points: "))
            end = int(input("Enter the range ending points: "))
            play = True
            break # Introducing break as this will break the loop whenever this block is completed

        except ValueError as e:
            '''If user enters different datatype, user is expected to enter values from the beginning i.e have to enter start value also even if it was of correct datatype.'''
            print("Please enter numbers only!!!")
            play = False
            #continue #this line is not required since it will continue if this block is exected
            
    #start, end = map(int, input("Enter the range starting & ending points: ").split())     # Initial code

    '''From here, the game begins'''
    user = User(start, end)
    while play == True:
        num = int(input("Guess the number: "))
        if num > end or num < start:
            '''This condition is checking if user has input the number from the desired range or not. if not, it will ask the user to only guess number from the desired range & prompt to enter the guess again.'''
            print("You have guessed number out of selected range ({} - {}). Please Try again".format(start, end))
            continue
        
        ''' "play" variable is storing a tuple in which 1st element will be the string of the status of game while the 2nd element tells if game will continue or not'''
        play = user.game(num) 
        print(play[0])
        play = play[1]

userBegin()
