from abc import ABC, abstractmethod
from Game import *
import tkinter as tk

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x300')
        self.root.resizable(False, False)
        self.root.title('Button Demo')
        self.text = " "#tk.StringVar() 
        self.count = 0
        self.buttonDict = {}

        self.buttonStart = tk.Button(self.root, text = "Play Game", height=2,width=10, command=self.clearOnPlayGame).grid(row=0, column=0, sticky= tk.W, pady=5, padx=5)
        self.buttonQuit = tk.Button(self.root, text = "Quit", height=2,width=5, command=quit).grid(row=0, column=1, sticky= tk.W, pady=5, padx=5)

    def playGame(self):
        for i in range(0,3):
            for j in range(0,3):
                self.count += 1
                self.cmd = lambda c=self.count: self.showX(c)   
                self.buttonDict["{0}".format(self.count)] = tk.Button(self.root, text= self.text, height=2,width=5, command=self.cmd)
                self.buttonDict["{0}".format(self.count)].grid(row=i, column=j, sticky= tk.W, pady=5, padx=5)
                
    def showX(self, count):
        turn = "X"
        self.buttonDict[str(count)]["text"] = turn 

        


    def clearOnPlayGame(self):
        list = self.root.grid_slaves()
        for l in list:
            l.destroy()
        self.playGame()

    def run(self):
        self.root.mainloop()
        print(self.buttonDict)


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



