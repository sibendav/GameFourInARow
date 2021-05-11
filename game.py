import copy
import alphaBetaPruning
#import random

VICTORY=10**20 #The value of a winning board (for max) 
LOSS = -VICTORY #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=4 #the length of winning seq.
COMPUTER=SIZE+1 #Marks the computer's cells on the board
HUMAN=1 #Marks the human's cells on the board

rows=6
columns=7


class game:
    board=[]
    size=rows*columns
    playTurn = HUMAN
    
     #Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''

def create(s):
        #Returns an empty board. The human plays first.
        #create the board
        s.board=[]
        for i in range(rows):
            s.board = s.board+[columns*[0]]
        
        s.playTurn = HUMAN
        s.size=rows*columns
        s.val=0.00001
    
        #return [board, 0.00001, playTurn, r*c]     # 0 is TIE

def cpy(s1):
        # construct a parent DataFrame instance
        s2=game()
        s2.playTurn = s1.playTurn
        s2.size=s1.size
        s2.board=copy.deepcopy(s1.board)
        print("board ", s2.board)
        return s2
    
    
    
def value(s):
#Returns the heuristic value of s
    
    if s.size>=rows*columns-4:
        return 0.1
    if s.size==0:
        return TIE

    zover=-0.1 # initialize the board grade in nagetive close to loss number, so that the computer always try to win
    
    for i in range(5, 0, -1): 
        for j in range(columns):
            if(s.board[i][j]!=0): # check for each one that is not 0/empty
                
                # *** ROW CHECKING  ***
                
                # check if the row have win situation , 4 in row
                if (j+3)<7 and s.board[i][j]==s.board[i][j+1] and s.board[i][j]==s.board[i][j+2] and s.board[i][j]==s.board[i][j+3]:
                        if(s.board[i][j]==COMPUTER):
                            return VICTORY
                        else:
                            return LOSS
                # check if the ROW is almost wins , 3 in row         
                if (j+3)<7 and ((s.board[i][j+1]==0 and s.board[i][j]==s.board[i][j+2] and s.board[i][j]==s.board[i][j+3]) or (s.board[i][j]==s.board[i][j+1] and 0==s.board[i][j+2] and s.board[i][j]==s.board[i][j+3]) or (s.board[i][j]==s.board[i][j+1] and s.board[i][j]==s.board[i][j+2] and 0==s.board[i][j+3])):
                        if(s.board[i][j]==COMPUTER):
                            if(s.playTurn==COMPUTER):
                                zover+=10000
                            zover+=(+1000)
                        else:
                            zover+=(-1000)
                # check if the row is close to almost wins , 2 in row              
                elif (j+3)<7 and ((s.board[i][j+1]==0 and 0==s.board[i][j+2] and s.board[i][j]==s.board[i][j+3]) or (0==s.board[i][j+1] and s.board[i][j]==s.board[i][j+2] and 0==s.board[i][j+3]) or (s.board[i][j]==s.board[i][j+1] and 0==s.board[i][j+2] and 0==s.board[i][j+3])):
                        if(s.board[i][j]==COMPUTER):
                            zover+=100
                        else:
                            zover+=(-100)   
                        
                                
                # ***  COLUMNS CHECKING   ***
                            
                # check if the columns have win situation             
                if (i-3)>=0 and s.board[i][j]==s.board[i-1][j] and s.board[i][j]==s.board[i-2][j] and s.board[i][j]==s.board[i-3][j]:
                        if(s.board[i][j]==COMPUTER):
                            return VICTORY
                        else:
                            return LOSS
                # check if the columns is almost wins , 3 in row          
                if (i-3)>=0 and ((s.board[i-1][j]==0 and s.board[i][j]==s.board[i-2][j] and s.board[i][j]==s.board[i-3][j]) or (s.board[i][j]==s.board[i-1][j] and 0==s.board[i-2][j] and s.board[i][j]==s.board[i-3][j]) or (s.board[i][j]==s.board[i-1][j] and s.board[i][j]==s.board[i-2][j] and 0==s.board[i-3][j])):
                        if(s.board[i][j]==COMPUTER):
                            if(s.playTurn==COMPUTER):
                                zover+=10000
                            zover+=(1000)
                        else:
                            zover+=(-1000)
                # check if the columns is close to almost wins , 2 in row              
                elif (i-3)>=0 and ((s.board[i-1][j]==0 and 0==s.board[i-2][j] and s.board[i][j]==s.board[i-3][j]) or (0==s.board[i-1][j] and s.board[i][j]==s.board[i-2][j] and 0==s.board[i-3][j]) or (s.board[i][j]==s.board[i-1][j] and 0==s.board[i-2][j] and 0==s.board[i-3][j])):
                        if(s.board[i][j]==COMPUTER):
                            zover+=(100)
                        else:
                            zover+=(-100)  
                                
                
                # *** SLANT CHECKING ***
                            
                # check if the slant have win situation            
                if (((j+3)<7 and (i-3)>=0) and s.board[i][j]==s.board[i-1][j+1] and s.board[i][j]==s.board[i-2][j+2] and s.board[i][j]==s.board[i-3][j+3]) or (((j-3)>=0 and (i-3)>=0) and s.board[i][j]==s.board[i-1][j-1] and s.board[i][j]==s.board[i-2][j-2] and s.board[i][j]==s.board[i-3][j-3]):
                        if(s.board[i][j]==COMPUTER):
                            return VICTORY
                        else:
                            return LOSS
                # check if the slant is almost wins , 3 in row          
                if ((j<4 and i>=3) and ((0==s.board[i-1][j+1] and s.board[i][j]==s.board[i-2][j+2] and s.board[i][j]==s.board[i-3][j+3]) or (s.board[i][j]==s.board[i-1][j+1] and 0==s.board[i-2][j+2] and s.board[i][j]==s.board[i-3][j+3]) or (s.board[i][j]==s.board[i-1][j+1] and s.board[i][j]==s.board[i-2][j+2] and 0==s.board[i-3][j+3]))) or ((j>=3 and i>=3) and ((0==s.board[i-1][j-1] and s.board[i][j]==s.board[i-2][j-2] and s.board[i][j]==s.board[i-3][j-3])or(s.board[i][j]==s.board[i-1][j-1] and 0==s.board[i-2][j-2] and s.board[i][j]==s.board[i-3][j-3])or(s.board[i][j]==s.board[i-1][j-1] and s.board[i][j]==s.board[i-2][j-2] and 0==s.board[i-3][j-3]))):                                                                                                                                                                                                                                                                                                                                                           
                        if(s.board[i][j]==COMPUTER):
                            if(s.playTurn==COMPUTER):
                                zover+=10000
                            zover+=(1000)
                        else:
                            zover+=(-1000)
                # check if the slant is close to almost wins , 2 in row              
                elif ((j<4 and i>=3) and ((0==s.board[i-1][j+1] and 0==s.board[i-2][j+2] and s.board[i][j]==s.board[i-3][j+3]) or (0==s.board[i-1][j+1] and s.board[i][j]==s.board[i-2][j+2] and 0==s.board[i-3][j+3]) or (s.board[i][j]==s.board[i-1][j+1] and 0==s.board[i-2][j+2] and 0==s.board[i-3][j+3])) )or ((j>=3 and i>=3) and ( (0==s.board[i-1][j-1] and 0==s.board[i-2][j-2] and s.board[i][j]==s.board[i-3][j-3]) or (0==s.board[i-1][j-1] and s.board[i][j]==s.board[i-2][j-2] and 0==s.board[i-3][j-3]) or (s.board[i][j]==s.board[i-1][j-1] and 0==s.board[i-2][j-2] and 0==s.board[i-3][j-3]))):                                                                                                                                                                                                                                                                                                                                                           
                        if(s.board[i][j]==COMPUTER):
                            zover+=(100)
                        else:
                            zover+=(-100)                                                       
        
    return zover  

   

def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.
        for r in range(rows):
            print("\n|",end="")
        #print("\n",len(s[0][0])*" --","\n|",sep="", end="")
            for c in range(columns):
                if s.board[r][c]==COMPUTER:
                    print("X|", end="")
                elif s.board[r][c]==HUMAN:
                    print("O|", end="")
                else:
                    print(" |", end="")

        print()

        for i in range(columns):
            print(" ",i,sep="",end="")

        print()
        
        val=value(s)

        if val==VICTORY:
            print("I won!")
        elif val==LOSS:
            print("You beat me!")
        elif val==TIE:
            print("It's a TIE")



def isFinished(s):
#Returns True if the game ended
        return value(s) in [LOSS, VICTORY, TIE] or s.size==0


def isHumTurn(s):
#Returns True if it is the human's turn to play
        return s.playTurn==HUMAN
    


def decideWhoIsFirst(s):
#The user decides who plays first
        if int(input("Who plays first? 1-me / anything else-you : "))==1:
            s.playTurn=COMPUTER
        else:
            s.playTurn=HUMAN
            
        return s.playTurn
        

def makeMove(s, c):
#Puts mark (for huma. or comp.) in col. c
#and switches turns.
#Assumes the move is legal.

        r=0
        while r<rows and s.board[r][c]==0:
            r+=1

        s.board[r-1][c]=s.playTurn # marks the board
        s.size -= 1 #one less empty cell
        if (s.playTurn == COMPUTER ):
            s.playTurn = HUMAN
        else:
            s.playTurn = COMPUTER

   
def inputMove(s):
#Reads, enforces legality and executes the user's move.

        #self.printState()
        flag=True
        while flag:
            c=int(input("Enter your next move: "))
            if c<0 or c>=columns or s.board[0][c]!=0:
                print("Illegal move.")

            else:
                flag=False
                makeMove(s,c)

        
def getNext(s):
#returns a list of the next states of s
        ns=[]
        for c in list(range(columns)):
            print("c=",c)
            if s.board[0][c]==0:
                print("possible move ", c)
                tmp=cpy(s)
                makeMove(tmp, c)
                print("tmp board=",tmp.board)
                ns+=[tmp]
                print("ns=",ns)
        print("returns ns ", ns)
        return ns

def inputComputer(s):    
        return alphaBetaPruning.go(s)
