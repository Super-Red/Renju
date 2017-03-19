from tkinter import *
from tkinter import messagebox

def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

def hasMove(board, player):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            if (hasMoveFromCell(board, player, row, col)):
                return True
    return False

def hasMoveFromCell(board, player, startRow, startCol):
    (rows, cols) = (len(board), len(board[0]))
    if (board[startRow][startCol] != 0):
        return False
    for dir in range(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            return True
    return False

def hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)):
            return False
        elif (board[row][col] == 0):
            # no blanks allowed in a sandwich!
            return False
        elif (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich
            i += 1
    return (i > 1)

def makeMove(board, player, startRow, startCol, canvas, chessList):
    # assumes the player has a legal move from this cell
    (rows, cols) = (len(board), len(board[0]))
    for dir in range(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            makeMoveInDirection(board, player, startRow, startCol, dir, canvas, chessList)
    board[startRow][startCol] = player
    chessList[startRow][startCol] = canvas.create_oval(33+40*startRow,33+40*startCol,67+40*startRow,67+40*startCol,fill=getPlayerLabel(player),width=0)

def makeMoveInDirection(board, player, startRow, startCol, dir, canvas, chessList):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich, so flip it!
            board[row][col] = player
            canvas.itemconfig(chessList[row][col], fill=getPlayerLabel(player))
            i += 1

def getPlayerLabel(player):
    labels = ["-", "black", "white"]
    return labels[player]

def isLegalMove(board, player, row, col):
    (rows, cols) = (len(board), len(board[0]))
    if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)): return False
    return hasMoveFromCell(board, player, row, col)

def winner(board):
    player1 = player2 = 0
    for i in range(len(board)):
        player1 = player1 + board[i].count(1)
        player2 = player2 + board[i].count(2)
    if (player1 > player2):
        return 'player1'
    elif(player1 < player2):
        return 'player2'
    else:
        return 'no one'
    
def playOthello(rows, cols):
    global currentPlayer
    Bwidth, Bheight = cols*40+70, rows*40+70
    root = Tk()
    root.title('Othella')
    root.geometry("%dx%d+300+50" % (Bwidth, Bheight))
    canvas = Canvas(root, width=Bwidth, height=Bheight+90, bd=3)
    # 使用rectangle和15条横竖线画出棋盘
    canvas.create_rectangle(30,30,30+cols*40,30+rows*40,fill="#E4C16B",width=2,outline="black")
    for i in range(rows):
        canvas.create_line(50+40*i,50,50+40*i,40*(cols-1)+50,fill="brown",width=1)
        canvas.create_line(50,50+40*i,40*(rows-1)+50,50+40*i,fill="brown",width=1)
    # create initial board
    board = make2dList(rows, cols)
    chessList = make2dList(rows, cols)
    board[rows//2][cols//2] = board[rows//2-1][cols//2-1] = 1
    board[rows//2-1][cols//2] = board[rows//2][cols//2-1] = 2
    chessList[rows//2][cols//2] = canvas.create_oval(33+40*(rows//2),33+40*(cols//2),67+40*(rows//2),67+40*(cols//2),fill='black',width=0)
    chessList[rows//2-1][cols//2-1] = canvas.create_oval(33+40*(rows//2-1),33+40*(cols//2-1),67+40*(rows//2-1),67+40*(cols//2-1),fill='black',width=0)
    chessList[rows//2-1][cols//2] = canvas.create_oval(33+40*(rows//2-1),33+40*(cols//2),67+40*(rows//2-1),67+40*(cols//2),fill='white', width=0)
    chessList[rows//2][cols//2-1] = canvas.create_oval(33+40*(rows//2),33+40*(cols//2-1),67+40*(rows//2),67+40*(cols//2-1),fill='white', width=0)
    printboard(board)
    # and play until the game is over
    def getMove(e):
        global currentPlayer, otherPlayer
        (row, col) = (round((e.x-50)/40),round((e.y-50)/40))        
        if (hasMove(board, currentPlayer) == False):
            if (hasMove(board, otherPlayer)):
                messagebox.showinfo("No legal move!  PASS!")
                (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
            else:
                messagebox.showinfo("No more legal moves for either player!")
        if (not isLegalMove(board, currentPlayer, row, col)):  
            messagebox.showinfo("That is not a legal move!  Try again.")
        else: 
            makeMove(board, currentPlayer, row, col, canvas, chessList)
            (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)      
    canvas.bind('<Button-1>',getMove)
    canvas.pack()
    root.mainloop()

def printboard(board):
    for i in range(len(board[0])):
        print (board[i])
    print ()

currentPlayer, otherPlayer = 1, 2
playOthello(8, 8)

