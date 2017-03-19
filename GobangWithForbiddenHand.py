'''
Game Name: Competitive Five
Created by Red_Chan
Finished on April 29th 2016
Fell free to contact me at fswccgh@126.com
'''

from tkinter import *
import copy

# create 4个非aliases的list避免destructive，分别用来存储玩家1、玩家2、整局、禁手的棋子分布,整局由8包着0
player1List = [] 
for i in range(23):player1List.append([0,]*23)
player2List = copy.deepcopy(player1List)
chessBoardList = copy.deepcopy(player1List)
for i in range(23):
    for j in range(23):
        if((i<4)or(i>18)or(j<4)or(j>18)):chessBoardList[i][j]=8
banHandList = copy.deepcopy(player1List) 
step = []

def numOfActive3(r,c,cl,bl):
    # row和column为要检查的坐标,cl是整局的list,bl是禁手的list,return活三的数量
    cl[r+4][c+4]=1
    number = 0
    # 连活三,分别为横竖斜四个方向检测该点是否有活三
    for i in range(2):
        if  ((cl[r+4][c+2+i]+cl[r+4][c+3+i]+cl[r+4][c+4+i]==3)and\
             (cl[r+4][c+1+i]+bl[r+4][c+1+i]+cl[r+4][c+5+i]+bl[r+4][c+5+i]==0)and\
            ((cl[r+4][c+i]+bl[r+4][c+i]==0)or(cl[r+4][c+6+i]+bl[r+4][c+6+i]==0))):number+=1
        elif((cl[r+2+i][c+4]+cl[r+3+i][c+4]+cl[r+4+i][c+4]==3)and\
             (cl[r+1+i][c+4]+bl[r+1+i][c+4]+cl[r+5+i][c+4]+bl[r+5+i][c+4]==0)and\
            ((cl[r+i][c+4]+bl[r+i][c+4]==0)or(cl[r+6+i][c+4]+bl[r+6+i][c+4]==0))):number+=1
        elif((cl[r+2+i][c+2+i]+cl[r+3+i][c+3+i]+cl[r+4+i][c+4+i]==3)and\
             (cl[r+1+i][c+1+i]+bl[r+1+i][c+1+i]+cl[r+5+i][c+5+i]+bl[r+5+i][c+5+i]==0)and\
            ((cl[r+i][c+i]+bl[r+i][c+i]==0)or(cl[r+6+i][c+6+i]+bl[r+6+i][c+6+i]==0))):number+=1
        elif((cl[r+2+i][c+6-i]+cl[r+3+i][c+5-i]+cl[r+4+i][c+4-i]==3)and\
             (cl[r+1+i][c+7-i]+bl[r+1+i][c+7-i]+cl[r+5+i][c+3-i]+bl[r+5+i][c+3-i]==0)and\
            ((cl[r+i][c+8-i]+bl[r+i][c+8-i]==0)or(cl[r+6+i][c+2-i]+bl[r+6+i][c+2-i]==0))):number+=1
    # 跳活三
    for i in range(3):
        if  ((cl[r+4][c+1+i]+cl[r+4][c+4+i]==2)and(cl[r+4][c+2+i]+cl[r+4][c+3+i]==1)and\
             (cl[r+4][c+i]+bl[r+4][c+i]+cl[r+4][c+5+i]+bl[r+4][c+5+i]==0)and\
            ((cl[r+4][c-1+i]+bl[r+4][c-1+i]==0)or(cl[r+4][c+6+i]+bl[r+4][c+6+i]==0))):number+=1
        elif((cl[r+1+i][c+4]+cl[r+4+i][c+4]==2)and(cl[r+2+i][c+4]+cl[r+3+i][c+4]==1)and\
             (cl[r+i][c+4]+bl[r+i][c+4]+cl[r+5+i][c+4]+bl[r+5+i][c+4]==0)and\
            ((cl[r-1+i][c+4]+bl[r-1+i][c+4]==0)or(cl[r+6+i][c+4]+bl[r+6+i][c+4]==0))):number+=1
        elif((cl[r+1+i][c+1+i]+cl[r+4+i][c+4+i]==2)and(cl[r+2+i][c+2+i]+cl[r+3+i][c+3+i]==1)and\
             (cl[r+i][c+i]+bl[r+i][c+i]+cl[r+5+i][c+5+i]+bl[r+5+i][c+5+i]==0)and\
            ((cl[r-1+i][c-1+i]+bl[r-1+i][c-1+i]==0)or(cl[r+6+i][c+6+i]+bl[r+6+i][c+6+i]==0))):number+=1
        elif((cl[r+1+i][c+7-i]+cl[r+4+i][c+4-i]==2)and(cl[r+2+i][c+6-i]+cl[r+3+i][c+5-i]==1)and\
             (cl[r+i][c+8-i]+bl[r+i][c+8-i]+cl[r+5+i][c+3-i]+bl[r+5+i][c+3-i]==0)and\
            ((cl[r-1+i][c+9-i]+bl[r-1+i][c+9-i]==0)or(cl[r+6+i][c+2-i]+bl[r+6+i][c+2-i]==0))):number+=1       
    return number

def numOfActive4(r,c,cl,bl):
    # 活四的数量
    cl[r+4][c+4]=1
    number = 0
    for i in range(3):
        if  ((cl[r+4][c+1+i]+cl[r+4][c+2+i]+cl[r+4][c+3+i]+cl[r+4][c+4+i]==4)and\
             (cl[r+4][c+i]+cl[r+4][c+5+i]==0)and(cl[r+4][c-1+i]+cl[r+4][c+6+i]==0)):number+=1
        elif((cl[r+1+i][c+4]+cl[r+2+i][c+4]+cl[r+3+i][c+4]+cl[r+4+i][c+4]==4)and\
             (cl[r+i][c+4]+cl[r+5+i][c+4]==0)and(cl[r-1+i][c+4]+cl[r+6+i][c+4]==0)):number+=1
        elif((cl[r+1+i][c+1+i]+cl[r+2+i][c+2+i]+cl[r+3+i][c+3+i]+cl[r+4+i][c+4+i]==4)and\
             (cl[r+i][c+i]+cl[r+5+i][c+5+i]==0)and(cl[r-1+i][c-1+i]+cl[r+6+i][c+6+i]==0)):number+=1
        elif((cl[r+1+i][c+7-i]+cl[r+2+i][c+6-i]+cl[r+3+i][c+5-i]+cl[r+4+i][c+4-i]==4)and\
             (cl[r+i][c+8-i]+cl[r+5+i][c+3-i]==0)and(cl[r-1+i][c+9-i]+cl[r+6+i][c+2-i]==0)):number+=1
    return number

def longConnection(r,c,cl,bl):
    # 长连
    for i in range(4):
        if  ((cl[r+4][c+i]==1)and(cl[r+4][c+1+i]==1)and(cl[r+4][c+2+i]==1)and\
             (cl[r+4][c+3+i]==1)and(cl[r+4][c+4+i]==1)and(cl[r+4][c+5+i]==5)):return True
        elif((cl[r+i][c+4]==1)and(cl[r+1+i][c+4]==1)and(cl[r+2+i][c+4]==1)and\
             (cl[r+3+i][c+4]==1)and(cl[r+4+i][c+4]==1)and(cl[r+5+i][c+4]==1)):return True
        elif((cl[r+i][c+i]==1)and(cl[r+1+i][c+1+i]==1)and(cl[r+2+i][c+2+i]==1)and\
             (cl[r+3+i][c+3+i]==1)and(cl[r+4+i][c+4+i]==1)and(cl[r+5+i][c+5+i]==5)):return True
        elif((cl[r+i][c+8-i]==1)and(cl[r+1+i][c+7-i]==1)and(cl[r+2+i][c+6-i]==1)and\
             (cl[r+3+i][c+5-i]==1)and(cl[r+4+i][c+4-i]==1)and(cl[r+5+i][c+3-i]==5)):return True

def refreshBanHandList(r,c,cl,bl):
    # 白手之后，通过前一手的黑手周围的八个方向的空格中，是否有禁手的存在，有则禁掉。（通过三三禁手or四四禁手or长连来判断）
    for i in range(9):
        if ((cl[r+4][c+i]==0)and(numOfActive3(r+4,c+i,cl,bl)>=2)or\
            (numOfActive4(r+4,c+i,cl,bl)>=2)or(longConnection(r+4,c+i,cl,bl))):bl[r+4][c+i]=1
        else:bl[r+4][c+i]=0
        if ((cl[r+i][c+4]==0)and(numOfActive3(r+i,c+4,cl,bl)>=2)or\
            (numOfActive4(r+i,c+4,cl,bl)>=2)or(longConnection(r+i,c+4,cl,bl))):bl[r+i][c+4]=1
        else:bl[r+i][c+4]=0
        if ((cl[r+i][c+i]==0)and(numOfActive3(r+i,c+i,cl,bl)>=2)or\
            (numOfActive4(r+i,c+i,cl,bl)>=2)or(longConnection(r+i,c+i,cl,bl))):bl[r+i][c+i]=1
        else:bl[r+i][c+i]=0
        if ((cl[r+i][c+8-i]==0)and(numOfActive3(r+i,c+8-i,cl,bl)>=2)or\
            (numOfActive4(r+i,c+8-i,cl,bl)>=2)or(longConnection(r+i,c+8-i,cl,bl))):bl[r+i][c+8-i]=1
        else:bl[r+i][c+8-i]=0
    return bl

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
    canvas = Canvas(root, width=900, height=700, bd=3)
    # 使用rectangle和15条横竖线画出棋盘
    canvas.create_rectangle(30,30,630,630,fill="#E4C16B",width=2,outline="black")
    for i in range(15):
        canvas.create_line(50+40*i,50,50+40*i,610,fill="brown",width=1)
        canvas.create_line(50,50+40*i,610,50+40*i,fill="brown",width=1)
    # 定义单击左键鼠标时的函数drawChess
    def drawChess(e):
        global banHandList
        # 确定鼠标点击点在二维数组中的row和col，因为网格点的坐标是50+40*i，因此round((坐标-50)/40)
        (row, col) = (round((e.x-50)/40),round((e.y-50)/40))
        # 如果该点已有棋子／超出棋盘范围，则跳过该点击操作
        if ((row>=0)&(row<=15)&(col>=0)&(col<=15)&(chessBoardList[row+4][col+4]==0)):
            # question 我使用step＝1再用自增的时候报错说我调用前未定义，不解，只好用list的append和len了
            step.append((row,col))
            if (len(step)%2==1):
                chessColor="black"
                player1List[row+4][col+4]=1
                chessBoardList[row+4][col+4]=1
            else:
                chessColor="white"
                player2List[row+4][col+4]=1
                chessBoardList[row+4][col+4]=5
            # 画出棋子，半径17，圆心为(50+40*row,50+40*col)
            canvas.create_oval(33+40*row,33+40*col,67+40*row,67+40*col,fill=chessColor,width=0)
            # 判断胜负 (黑手下完后判断是否下了禁手，白手下完后refresh禁手的list)
            if (chessColor=="black"):
                if (banHandList[row][col]==1):
                    Message(text="Player2 has won!").pack()
                elif (isWin(row,col,player1List)):
                    Message(text="Player1 has won!").pack()
            else:
                banHandList = refreshBanHandList(step[-2][0],step[-2][1],chessBoardList,banHandList)
                if(isWin(row,col,player2List)):
                    Message(text="Player2 has won!").pack()
    canvas.bind('<Button-1>',drawChess)
    canvas.pack()
    root.mainloop()

drawChessBoard()