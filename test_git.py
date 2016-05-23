import sys, random, copy

class Minesweeper(object):
  
  def __init__(self):
    self.board=[
      ["-","-","-"],
      ["-","-","-"],
      ["-","-","-"]
    ]
  
  def playsLeft(self,board):
    return sum(x.count("-") for x in board)
  
  def printFeld(self,board):
    for i in board:
      print("")
      for x in i:
        print(x,end=" ")
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
    if self.playsLeft(board) == 0:
      self.printFeld(board)
      print(self.calcPoints(board))
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
    print(scores)
    print(best)
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
    
lol = Minesweeper()
lol.letsPlay()

#lol.board[0][2]="X"
#print(lol.goDeeper(lol.board,"O"))


#print(lol.evalMoves(lol.board))
#print(lol.possibleMoves(lol.board))
#print lol.evalMoves(lol.board)
#print lol.calcPoints(lol.board)
#sys.stderr.write("\x1b[2J\x1b[H")