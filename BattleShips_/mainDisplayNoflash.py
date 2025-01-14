import time
import os 
import sys ,tty
import asyncio
import threading
import random
from cfonts import render, say
from Grid import*
from Display import*
from Overlap import *
from Place import *
from Inputs import *
from Computer import *
from AttackDisplay import *
from Attack import *
from ComputerAttack import *
from dataValidation import *
from alreadyPlaced import *
from WinCheck import *
from ResumeGame import *
tty.setcbreak(sys.stdin)



'''
def enter():
    global enterCheck
    while True:
       key = ord(sys.stdin.read(1))
       if key == 10:
        enterCheck = True
'''






def mainP1(board):
    x = 0
    y = 0
    
    NotPlaced = True
    enterCheck = False
    delCheck = False
    shipAxis = 'horizontal'
    shipType = 'warship'
   
    warshipTotal = 3
    submarineTotal = 2
    temp = board[y][x]
    newTemp = ' '
    while NotPlaced:
        print(x+1,y+1)
        
        Display(board,warshipTotal,submarineTotal)
        inputs = usrInp(shipAxis,shipType)
        enterCheck = inputs[1]
        delCheck = inputs[2]
        Input = inputs[0]
        #print(Input)
        shipAxis = inputs[3]
        shipType = inputs[4]
        end = inputs[5]
       
        if 67 in Input:
            
            x += 1
            if x == 8:
                x = 0
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'
            board[y][x-1] = temp
            Input = [0,0,0] 
        if 68 in Input:
            
            x -= 1
            
            if x == -1:
                x = 7
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'

            if x == 7:
                board[y][0] = temp
            else:
                board[y][x+1] = temp
            
            Input = [0,0,0] 
        if 66 in Input:
            
            y += 1
            if y == 8:
                y = 0
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'
            board[y-1][x] = temp
            Input = [0,0,0] 
        if 65 in Input:

            y -= 1
            if y == -1:
                y = 7
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'
            if y == 7:
                board[0][x] = temp
            else:
                board[y+1][x] = temp
            Input = [0,0,0] 
		#Board[y+1][x] = ' '
        
        #print(enterCheck)
        #print(delCheck)
       

        if enterCheck == True:
            #print(newTemp)
            ShipCount = place(x,y,board,enterCheck,'enter',shipType,shipAxis,warshipTotal,submarineTotal,newTemp)
            enterCheck = False
            warshipTotal = ShipCount[0]
            submarineTotal = ShipCount[1]
            newTemp = ShipCount[2]
        if delCheck == True:
            ShipCount = place(x,y,board,delCheck,'del',shipType,shipAxis,warshipTotal,submarineTotal,newTemp)
            delCheck = False
            warshipTotal = ShipCount[0]
            submarineTotal = ShipCount[1]
            newTemp = ShipCount[2]
        if  end == True and warshipTotal == 0 and submarineTotal == 0:
            NotPlaced = False
            Input = [0,0,0] 
        os.system('clear')


        temp = newTemp
        
        #print(temp)
    #print(board)
    return board

#mainP1()








def mainP2(state,board,attackBoard,cBoard):
    os.system('reset')
    notWon = True
    playerHits = 0
    compHits = 0
    chars = ['A','B','C','D','E','F','G','H']
    stop = False
    pause =  False
    if (os.path.isfile("player.csv") == True and os.path.isfile("computer.csv") == True and os.path.isfile("attackDisplay.csv") == True)  or state == False:
        if state == True:
            board = openSave('player')
            cBoard = openSave('computer')
            attackBoard = openSave('attackDisplay')
            Data =  TurnData()
            playerHits = Data[2]
            compHits = Data[1]
        while notWon:
            
            attackDisplay(board,attackBoard)
            print('\n')
            alreadyPlaced = True
            
            while alreadyPlaced:
                x = Xcord_data_validation('                                            input x cord:')
                y = int_data_validation('                                            input y cord: ')
                if x == 'confirmed' or y == 'confirmed':
                    pause = True
                    alreadyPlaced = False
                    notWon =  False
                    save(board,'player')
                    save(cBoard,'computer')
                    save(attackBoard,'attackDisplay')
                    SaveTurn(compHits,playerHits)
                else:
                    y = y-1
                    alreadyPlaced = AlreadyPlaced(x,y,attackBoard,1)


            if pause == False:
                playerHits = attack(y,x,cBoard,attackBoard,playerHits)
                won = check(playerHits,compHits)
                if won == True and stop == False:
                    notWon = False
                    stop = True
                alreadyPlaced =  True
                while alreadyPlaced:
                    y2 = random.randrange(0,8)-1
                    x2 = random.choice(chars)
                    alreadyPlaced = AlreadyPlaced(x2,y2,board,0)
                compHits = CompAttack(y2,x2,board,compHits)
                save(board,'player')
                save(cBoard,'computer')
                save(attackBoard,'attackDisplay')
                SaveTurn(compHits,playerHits)
                won = check(playerHits,compHits)
                if won[0] == True and stop == False:
                    state = False
                    notWon = False
                    stop = True
                    os.system('clear')
                    if won[1] == 'player':
                        Output = render('YOU WON', align='center',colors=['red','blue'], font = 'shade')
                        print(Output)
                        time.sleep(3)
                    if won[1] == 'computer':
                        Output = render('better luck next time', align='center',colors=['red','blue'], font = 'shade')
                        print(Output)
                        time.sleep(3)
                    os.remove("attackDisplay.csv")
                    os.remove("computer.csv")
                    os.remove("player.csv")
                    
                    

                
            os.system('clear')
    else:
        Output = render('No save data found ', align='center',colors=['red','blue'], font = 'shade')
        print(Output)
        time.sleep(3)
        os.system('clear')
        
    return state
#mainP2()
