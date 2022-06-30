n=int(input("Enter the value of n"))
board=[]

 def getBoard():
     foriin range (n):
          nthList=[]
           forjin range (n):
                nthList.append (0)
          board.append (nthList)

def printBoard():
   foriin range (n):
      forjin range (n):
          print (board[i][j], end="")
      print("")

def isSafe (row, col):
    foriin range (n):
        if board[row] [i] == 1:
             return False
    forjin range (n):
        if board[j] [col] == 1:
             return False

def Put(n, count):
   if count == n:
       return True
   foriin range (n):
       forjin range (n):
           if isSafe (i, j):
               board[i][j]=1
               count=count+1
               if Put(n, count) == True:
                   return True
               board[i] [j]=0
               count=count-1
   return False

getBoard ()
Put (n, 0)
printBoard()
