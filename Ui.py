from abc import ABC, abstractmethod
from Game import *

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self.game = Game()

    def printBoard(self, board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])

    def run(self):   
        self.printBoard(self.game.theBoard)
        self.move = input(f"It is {self.game.turn}'s Turn please make a move: ")
        hasFinished = self.game.play(self.move)
        if hasFinished == False:
            print("That space is already taken please select another: ")
        elif hasFinished == "Winner":
            print(f"The winner is {self.game.turn} on turn {self.game.count}!!!")
            self.printBoard(self.game.theBoard)
            quit()
        elif hasFinished == "Draw":
            self.printBoard(self.game.theBoard)
            print("The game has ended in a draw!")
            quit()
        self.run()



