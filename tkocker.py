from tkinter import *
import time
import sys, random, copy

class Minesweeper(object):
  
  def __init__(self):
    self.flipped = False
  
    self.board=[
      ["-","-","-"],
      ["-","-","-"],
      ["-","-","-"]
    ]
	
  def resetBoard(self):
    self.board=[
      ["-","-","-"],
      ["-","-","-"],
      ["-","-","-"]
    ]
  
  def playsLeft(self,board):
    return sum(x.count("-") for x in board)
  
  def printFeld(self,board):
    for row, item in enumerate(board):
      for col, item2 in enumerate(item):
        knopf = "button"+str(row)+str(col)
        rofl = getattr(GUI, knopf)
        rofl.config(text=item2)
        root.update()
    print(" ")

  def calcPoints(self,board):
    winCombis = [
      [[0,0],[0,1],[0,2]],
      [[1,0],[1,1],[1,2]],
      [[2,0],[2,1],[2,2]],
      [[0,0],[1,0],[2,0]],
      [[0,1],[1,1],[2,1]],
      [[0,2],[1,2],[2,2]],
      [[0,0],[1,1],[2,2]],
      [[0,2],[1,1],[2,0]]
    ]
    
    for i in winCombis:
      winx=True
      wino=True
      for c in i:
        if board[c[0]][c[1]]!="X":
          winx=False
        if board[c[0]][c[1]]!="O":
          wino=False
      if winx==True:
        return 10
      if wino==True:
        return -10
    if self.playsLeft(board)==0:
      return 0
    return None
    
  def possibleMoves(self,board):
    moves=[]
    for row in range(0,3):
      for pos in range(0,3):
        if board[row][pos]=="-":
          moves.append([row,pos])
    return moves
  
  def goDeeper(self,board,player):
    sum = []
    sum.append(self.calcPoints(board))
    #if self.playsLeft(board) == 0:
      #self.printFeld(board)
      #print(self.calcPoints(board))
    if self.playsLeft(board)>0 and self.calcPoints(board)==None:
      for move in self.possibleMoves(board):
        x = copy.deepcopy(board)
        if player == "X":
          x[move[0]][move[1]]="X"
          sum.append(self.goDeeper(x,"O")) 
        if player == "O":
          x[move[0]][move[1]]="O"
          sum.append(self.goDeeper(x,"X"))
    if player == "X":
      return max(x for x in sum if x is not None)
    if player == "O":
      return min(x for x in sum if x is not None)
  
  def evalMoves(self,board):
    scores =[]
    for move in self.possibleMoves(board):
      x = copy.deepcopy(board)
      x[move[0]][move[1]]="X"
      scores.append([self.goDeeper(x,"O"),move])
    return scores
  
  def makePlay(self): 
    scores = self.evalMoves(self.board)
    best = scores[scores.index(max(scores))][1]
    #print(scores)
    #print(best)
    self.board[best[0]][best[1]]="X"
  
  def letsPlay(self):
    self.printFeld(self.board)
    while self.playsLeft(self.board)>0 and self.calcPoints(self.board)==None:
      coords = eval(input('Player O, make play, like 0,2 ... '))
      self.board[coords[0]][coords[1]]="O"
      print("You played:")
      self.printFeld(self.board)
      if self.playsLeft(self.board)>0 and self.calcPoints(self.board)==None:
        self.makePlay()
        print("CPU played:")
        self.printFeld(self.board)
    
  def cpuvcpu(self):
    self.board[random.randint(0, 2)][random.randint(0, 2)]="O"
    self.printFeld(self.board)
    while self.calcPoints(self.board) is None:
      self.makePlay()
      self.flipBoard()
      if lol.flipped:
        self.flipBoard()
        self.printFeld(self.board)
        self.flipBoard()
      else:
        self.printFeld(self.board)
      time.sleep(2)
    self.resetBoard()

  def flipBoard(self):
    if self.flipped:
      player1 = "O"
      player2 = "X"
      self.flipped = False
    else:
      player1 = "X"
      player2 = "O"
      self.flipped = True
    for pos1,cont1 in enumerate(self.board):
      for pos2,con2 in enumerate(cont1):
        if self.board[pos1][pos2] == player1:
          self.board[pos1][pos2] = player2
        elif self.board[pos1][pos2] == player2:
          self.board[pos1][pos2] = player1

root = Tk()
lol = Minesweeper()

class GUI(Frame):
    def __init__(self, master=None,
                 width=100, height=300):
        Frame.__init__(self, master,
                       width=width, height=height)
    button00 = Button(root, text="-", height = 2, width = 5)
    button00.grid(row=1, column=1)
    button01 = Button(root, text="-", height = 2, width = 5)
    button01.grid(row=1, column=2)
    button02 = Button(root, text="-", height = 2, width = 5)
    button02.grid(row=1, column=3)
    button10 = Button(root, text="-", height = 2, width = 5)
    button10.grid(row=2, column=1)
    button11 = Button(root, text="-", height = 2, width = 5)
    button11.grid(row=2, column=2)
    button12 = Button(root, text="-", height = 2, width = 5)
    button12.grid(row=2, column=3)
    button20 = Button(root, text="-", height = 2, width = 5)
    button20.grid(row=3, column=1)
    button21 = Button(root, text="-", height = 2, width = 5)
    button21.grid(row=3, column=2)
    button22 = Button(root, text="-", height = 2, width = 5)
    button22.grid(row=3, column=3)
    buttonGO = Button(root, text="GO", height = 2, width = 5, command = lol.cpuvcpu)
    buttonGO.grid(row=4, column=2)

root.mainloop()
	
#lol.letsPlay()
#lol.cpuvcpu()

#print(lol.goDeeper(lol.board,"O"))
#print(lol.evalMoves(lol.board))
#print(lol.possibleMoves(lol.board))
#print lol.evalMoves(lol.board)
#print lol.calcPoints(lol.board)
#sys.stderr.write("\x1b[2J\x1b[H")









