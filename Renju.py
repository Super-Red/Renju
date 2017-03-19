'''
Game Name: Competitive Renju without ban hands
Created by Red_Chan
Finished on April 29th 2016
Beautified on May 19th 2016
Fell free to contact me at fswccgh@126.com
'''

from tkinter import *
from tkinter import messagebox
import copy

# create 3个非aliases的list避免destructive，分别用来存储玩家1、玩家2、整局的棋子分布
player1List = [] 
for i in range(23):player1List.append([0,]*23)
player2List = copy.deepcopy(player1List)
chessBoardList = copy.deepcopy(player1List)
step = []

def isWin(r,c,cl):
    # row和column作为刚下的棋的坐标，cl是每个玩家的chesslist
    for i in range(5):
        # 计算刚下一步棋的横向是否构成赢棋，赢棋结果为1
        rowresult = cl[r+4][c+i]*cl[r+4][c+1+i]*cl[r+4][c+2+i]*cl[r+4][c+3+i]*cl[r+4][c+4+i]
        # 计算纵向是否构成赢棋，赢棋结果为1
        colresult = cl[r+i][c+4]*cl[r+1+i][c+4]*cl[r+2+i][c+4]*cl[r+3+i][c+4]*cl[r+4+i][c+4]      
        # 计算从左向右的对角线
        ltrresult = cl[r+i][c+i]*cl[r+1+i][c+1+i]*cl[r+2+i][c+2+i]*cl[r+3+i][c+3+i]*cl[r+4+i][c+4+i]
        # 计算从右向左的对角线
        rtlresult = cl[r+i][c+8-i]*cl[r+1+i][c+7-i]*cl[r+2+i][c+6-i]*cl[r+3+i][c+5-i]*cl[r+4+i][c+4-i]
        # 只要四个中其中一个非零，就能构成赢棋
        if (rowresult+colresult+ltrresult+rtlresult>0):return True
    return False

def drawChessBoard():
    root = Tk()
    root.title("五子棋")
    root.geometry("670x720+300+50")
    canvas = Canvas(root, width=670, height=630, bd=3)
    canvas2 = Canvas(root, width=300, height=50, bd=3, bg="#E4C16B")
    # 使用rectangle和15条横竖线画出棋盘
    canvas.create_rectangle(30,30,630,630,fill="#E4C16B",width=2,outline="black")
    canvas2Chess = canvas2.create_oval(16,16,46,46,fill="black",width=0)
    canvas2Player = canvas2.create_text(176,30,font="Monaco 25 bold",text="Player1's turn",fill='black')
    for i in range(15):
        canvas.create_line(50+40*i,50,50+40*i,610,fill="brown",width=1)
        canvas.create_line(50,50+40*i,610,50+40*i,fill="brown",width=1)
    # 定义单击左键鼠标时的函数drawChess
    def drawChess(e):
        # 确定鼠标点击点在二维数组中的row和col，因为网格点的坐标是50+40*i，因此round((坐标-50)/40)
        (row, col) = (round((e.x-50)/40),round((e.y-50)/40))
        # 如果该点已有棋子／超出棋盘范围，则跳过该点击操作
        if ((row>=0)&(row<=15)&(col>=0)&(col<=15)&(chessBoardList[row+4][col+4]==0)):
            # question 我使用step＝1再用自增的时候报错说我调用前未定义，不解，只好用list的append和len了
            step.append((row,col))
            chessBoardList[row+4][col+4]=1
            if (len(step)%2==1):
                chessColor="black"
                player1List[row+4][col+4]=1
            else:
                chessColor="white"
                player2List[row+4][col+4]=1
            # 画出棋子，半径17，圆心为(50+40*row,50+40*col)
            canvas.create_oval(33+40*row,33+40*col,67+40*row,67+40*col,fill=chessColor,width=0)
            # 判断胜负
            if (isWin(row,col,player1List)):
                messagebox.askyesnocancel("Congratulations~","Player1 has won!\nWanna try again?")
            elif (isWin(row,col,player2List)):
                messagebox.askyesnocancel("Congratulations~","Player2 has won!\nWanna try again?")
        changeState(len(step))
    # 提示选手
    def changeState(stepsNum):
        if (stepsNum%2==1):
            canvas2.itemconfig(canvas2Chess, fill='white')
            canvas2.itemconfig(canvas2Player, text="Player2's turn",fill='white')
        else:
            canvas2.itemconfig(canvas2Chess, fill='black')
            canvas2.itemconfig(canvas2Player, text="Player1's turn",fill='black')

    canvas.bind('<Button-1>',drawChess)
    canvas.pack()
    canvas2.pack()
    root.mainloop()

drawChessBoard()