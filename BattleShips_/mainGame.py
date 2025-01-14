from cfonts import render, say
import os
import keyboard
import time
import threading
import asyncio
import sys ,tty
#from mainDisplay import *
from mainDisplayNoflash import *
tty.setcbreak(sys.stdin)
Input = [0,0,0]
enterCheck = False
def DisplayMenu(selection):
    output = render('Battle Ships', align='center',gradient = ['blue','yellow'])
    print(output)

    if selection == 1:
        select1 ='simple'
        select2 ='chrome'
        select3 ='chrome'
        select4 ='chrome'
    if selection == 2:
        select2 ='simple'
        select1 ='chrome'
        select3 ='chrome'
        select4 ='chrome'
    if selection == 3:
        select3 ='simple'
        select2 ='chrome'
        select1 ='chrome'
        select4 ='chrome'
    if selection == 4:
        select4 ='simple'
        select2 ='chrome'
        select3 ='chrome'
        select1 ='chrome'
    if selection == 0:
        select1 ='chrome'
        select2 ='chrome'
        select3 ='chrome'
        select4 ='chrome'

    button1 = render('new game', align='center',gradient = ['blue','yellow'] ,font =select1)
    button2 = render('resume game', align='center',gradient = ['blue','yellow'] ,font = select2)
    button3 = render('quit game', align='center',gradient = ['blue','yellow'] ,font = select3)
    button4 = render('instructions', align='center',gradient = ['blue','yellow'] ,font =select4)
    print(button1)
    print(button2)
    print(button3)
    print(button4)

def moveSelection(State ):
    global Input
    if  65 in Input :
        State = State-1
        if State ==0 or State == -1:
            State = 4
    if  66 in Input:
        State = State+1
        if State ==5:
            State = 1
    Input = [0,0,0]
    
    return State
def UsrInp():
    notRecived = True
    global Input
    global enterCheck
    keyTypes = [65,66,67,68,91,27]
    for i in range(3):
        key = ord(sys.stdin.read(1))
        if key in keyTypes:
            if key not in Input:
                Input[i] = key
        else:
            if key == 10:
                enterCheck = True
            break

def menu():
    selection = 0
    OptionNotSelected = True
    global Input
    global enterCheck
    stop = False
    while OptionNotSelected:
        
        DisplayMenu(selection)
        
        UsrInp()
        #print(Input)
        #print(enterCheck)
        
        if enterCheck == True and stop == False :
            #print('TRue')
            if selection != 0 :
                stop =True
                OptionNotSelected = False
            enterCheck = False
        if stop == False:
            Selection = moveSelection(selection)
            selection = Selection
            #print(selection)
            os.system('clear')
    os.system('clear')
    #print(selection)
    return selection
        
        
#t1 = threading.Thread(target = usrInp)  
#t2 =  threading.Thread(target = mainGame) 
#t1.start()
#t2.start()


def Modes(option):
    
    '''
    if option== 1:
        t2 =  threading.Thread(target = mainP1)
        t1 = threading.Thread(target = usrInp) 
        t2.start()
        t1.start()
        t1.join()
        t2.join()
        mainP2()
    '''
    if option== 1:
        board = Grid(8,8)
        Board = mainP1(board)
        attackBoard = Grid(8,8)
        cBoard = Grid(8,8)
        sCount = 2
        wCount = 3
        for i in range(5):
            count = CompBoard(cBoard,wCount,sCount)
            wCount = count[0]
            sCount = count[1]
        State = mainP2(False,Board,attackBoard,cBoard)
        tty.setcbreak(sys.stdin)
    if option == 3:
        Output = render('Thank You For Playing BattleShips', align='center',colors=['red','blue'], font = 'shade')
        print(Output)
        exit()
        
    if option == 4:
        Noexit = True
        #os.system('reset')
        Font = 'console'
        while Noexit:
            Output = render('Instructions', align='center',colors=['red','blue'], font = 'slick')
            print(Output)
            line1 = render('Battleships is a strategy game where you are playing against the computer', align='center',colors=['blue'], font = Font)
            print(line1)
            line3 = render('You have 3 warships and 2 submarines,ships can be placed by clicking enter key ', align='center',colors=['blue'], font = Font)
            print(line3)
            line5 = render('Press W key to place a Warship and  Press S to place a Submarine  ', align='center',colors=['blue'], font = Font)
            print(line5)
            line6 = render('Press H key to place a Ship Horizontal and  Press V to place a Ship Verticle ', align='center',colors=['blue'], font = Font)
            print(line6)
            line7 = render('Ships can be deleted by pressing backspace whilst hovering over the highlighted color  ship ', align='center',colors=['blue'], font =Font)
            print(line7)
            line8 = render('Once all ships placed press C key to continue ', align='center',colors=['blue'], font = Font)
            print(line8)
            line10 = render(' you can now attack the computer  a yellow is a miss and red is a hit', align='center',colors=['blue'], font = Font)
            print(line10)
            line11 = render("The first one to destroy all the opponent's ships win", align='center',colors=['blue'], font = Font)
            print(line11)
            line12 = render('Press backspace key to go back', align='center',colors=['blue'], font = Font)
            print(line12)
            key = ord(sys.stdin.read(1))
            if key == 127:
                Noexit = False
            os.system('clear')
    if  option == 2:
        mainP2(True,'prev','prev','prev')
        tty.setcbreak(sys.stdin)

def MainGame():
    while True:
        option = menu()
        Modes(option)
MainGame()




    
