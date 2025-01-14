import random
from Overlap import *

'''
program creates the computer board
with ships placed
'''

def CompBoard(board, wCount,sCount):
    NotPlaced = True
    
    while NotPlaced:
        axis = ['x','y']
        Choice = random.choice(axis)
        ship  = ['warship','submarine']
        shipType = random.choice(ship)
        #print(Choice)
        mainColor = ['\x1b[38;2;15;82;186m\u2588','\x1b[38;2;75;104;185m\u2588','\x1b[38;2;0;181;226m\u2588','\x1b[38;2;0;138;216m\u2588']
        if Choice == 'x' and shipType == 'warship' and wCount>0:
            x = random.randint(1,5)
            y = random.randint(0,7)
            #print(x,y)
            overlap = checkOverlap(board,x,y,'warship')
            if overlap == False:
                board[y][x] =mainColor[0]
                board[y][x+1] =mainColor[1]
                board[y][x+2] =mainColor[1]
                board[y][x-1] =mainColor[1]
                NotPlaced = False
                wCount -=1
        if Choice == 'x' and shipType == 'submarine' and sCount:
            x = random.randint(1,6)
            y = random.randint(0,7)
            #print(x,y)
            overlap = checkOverlap(board,x,y,'submarine')
            if overlap == False:
                board[y][x] =mainColor[2]
                board[y][x+1] =mainColor[3]
                board[y][x-1] =mainColor[3]
                NotPlaced = False
                sCount -=1
                
        
        
        if Choice == 'y' and shipType == 'warship' and wCount >0:
            y = random.randint(1,5)
            x = random.randint(0,7)
            #print(x,y)
            overlap = checkOverlap(board,x,y,'warship')
            if overlap == False:
                board[y][x] =mainColor[0]
                board[y+2][x] =mainColor[1]
                board[y+1][x] =mainColor[1]
                board[y-1][x] =mainColor[1]
                NotPlaced = False
                wCount -=1
        if Choice == 'y' and shipType == 'submarine' and sCount>0:
            y = random.randint(1,6)
            x = random.randint(0,7)
            #print(x,y)
            overlap = checkOverlap(board,x,y,'submarine')
            if overlap == False:
                board[y][x] =mainColor[2]
                board[y+1][x] =mainColor[3]
                board[y-1][x] =mainColor[3]
                NotPlaced = False
                sCount -=1
    return [wCount,sCount]