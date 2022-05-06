from abc import ABC, abstractmethod
from Game import *
import tkinter as tk

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        self.game = Game()
        self.root = tk.Tk()
        self.root.geometry('300x300')
        self.root.resizable(False, False)
        self.root.title('Button Demo')
        self.text = " "
        self.count = 0
        self.buttonDict = {}
        self.state = tk.NORMAL
        self.buttonStart = tk.Button(self.root, text = "Play Game", height=2,width=10, command=self.clearOnPlayGame).grid(row=0, column=0, sticky= tk.W, pady=5, padx=5)
        self.buttonQuit = tk.Button(self.root, text = "Quit", height=2,width=10, command=quit).grid(row=1, column=0, sticky= tk.W, pady=5, padx=5)

    def playGame(self):
        for i in range(0,3):
            for j in range(0,3):
                self.count += 1
                cmd = lambda c=self.count: self.showX(c)   
                self.buttonDict["{0}".format(self.count)] = tk.Button(self.root, text= self.text, height=3,width=6, command=cmd, state=self.state)
                self.buttonDict["{0}".format(self.count)].grid(row=i, column=j, sticky= tk.W, pady=5, padx=5)
        self.playAgain = tk.Button(self.root, text = "Play again", height=2,width=10, command=self.restartGame).grid(row=0, column=4, sticky= tk.W, pady=5, padx=5)
        self.buttonQuit = tk.Button(self.root, text = "Quit", height=2,width=10, command=quit).grid(row=1, column=4, sticky= tk.W, pady=5, padx=5)        
        tk.Label(self.root, text=f"{self.game.turn}'s turn").grid(row=4, column=1)
        tk.Label(self.root, text=f"WINS X: {self.game.xAmountWin} O: {self.game.oAmountWin}").grid(row=2, column=4) 

    def restartGame(self):
        self.firstPlay = False
        self.game.turn = "X"
        self.count = 0
        self.game.count = 1
        self.clearOnPlayGame()

    
                
    def showX(self, count):
        try:
            self.buttonDict[str(count)]["text"] = self.game.turn 
            self.game.switchTurn()
        except:
            print("You are unable to go there")
        self.game.theBoard = self.buttonDict
        tk.Label(self.root, text=f"{self.game.turn}'s turn").grid(row=4, column=1) 
        try:
            self.buttonDict[str(count)] = self.buttonDict[str(count)]["text"]
        except:
            pass

        if self.game.checkWin() == "X" or self.game.checkWin() == "O":
            if self.game.checkWin() == "O":
                self.game.xAmountWin += 1
            elif self.game.checkWin() == "X":
                self.game.oAmountWin += 1
            #Make win window
            for i in range(len(self.buttonDict)):
                self.buttonDict[str(i+1)] = " "
            new= tk.Toplevel(self.root)
            new.geometry("100x100")
            new.title("Winner")
            self.game.switchTurn()
            tk.Label(self.root, text=f"WINS X: {self.game.xAmountWin} O: {self.game.oAmountWin}").grid(row=2, column=4) 
            tk.Label(new, text=f"{self.game.turn} Is the Winner!").pack(pady=30)
            tk.Button(new, text = "Ok", height=2,width=10, command=quit).pack(pady=30)
        elif self.game.count == 10:
            #Make draw window
            self.game.count += 1      
            new= tk.Toplevel(self.root)
            new.geometry("100x100")
            new.title("Draw")
            tk.Label(new, text=f"It is a Draw!").pack(pady=30)
    

        


    def clearOnPlayGame(self):
        list = self.root.grid_slaves()
        for l in list:
            l.destroy()
        self.playGame()

    def run(self):
        self.root.mainloop()


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