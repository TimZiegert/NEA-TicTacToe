class Game:

    def __init__(self):
        self.theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
        self.turn = "X"
        self.count = 1
        self.xAmountWin = 0
        self.oAmountWin = 0

    def __repr__(self):
        pass

    def checkWin(self):
        if self.theBoard['1'] == self.theBoard['2'] == self.theBoard['3'] != ' ': 
            return self.turn                
        elif self.theBoard['4'] == self.theBoard['5'] == self.theBoard['6'] != ' ': 
            return self.turn
        elif self.theBoard['7'] == self.theBoard['8'] == self.theBoard['9'] != ' ':
            return self.turn
        elif self.theBoard['1'] == self.theBoard['4'] == self.theBoard['7'] != ' ': 
            return self.turn
        elif self.theBoard['2'] == self.theBoard['5'] == self.theBoard['8'] != ' ': 
            return self.turn
        elif self.theBoard['3'] == self.theBoard['6'] == self.theBoard['9'] != ' ': 
            return self.turn
        elif self.theBoard['7'] == self.theBoard['5'] == self.theBoard['3'] != ' ': 
            return self.turn
        elif self.theBoard['1'] == self.theBoard['5'] == self.theBoard['9'] != ' ': 
            return self.turn
        else:
            return None

    def play(self,place):
        if self.theBoard[place] == ' ':
            self.theBoard[place] = self.turn
        else:
            return False

        if self.count >= 5:
            if self.checkWin() == "X" or self.checkWin() == "O":
                return "Winner"
            elif self.count == 9:
                return "Draw"
            else:
                pass 
        self.switchTurn()

    def switchTurn(self):
        self.count += 1
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"





if __name__ == "__main__":
    pass

if True == True:
    pass