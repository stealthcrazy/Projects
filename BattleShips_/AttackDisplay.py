import time
import os 
import sys ,tty
import asyncio
import threading
import random
from cfonts import render, say

'''
program displays the attack display 
attack display is a blank grid for attacking 
contains your grid and blank attack grid
'''

def attackDisplay(board,attackBoard):
    os.system('clear') # clears the console
    row = 0
    output = render('Battle Ships', align='center',colors = ['blue','yellow'] ,font = 'simple3d')# outputs Battle Ships in 3d font 
    print(output)
    print('                                              A     B    C    D    E    F    G    H               A     B    C    D    E    F    G    H ') # horizontal grid cordinates
    for i in range(8): # for loop to generate both displays next to each other
        string = f'{i+1}\x1b[38;2;255;255;255m|'
        string2 =  f'{i+1}\x1b[38;2;255;255;255m|'
        #print(b1[i],b2[i])
        for j in range(8): # displays the rows 
            string += ' '+board[i][j]+'  \x1b[38;2;255;255;255m|'
            string2 += ' '+attackBoard[i][j]+'  \x1b[38;2;255;255;255m|'
        print('                                            '+string +'         '+string2) # prints the rows with each column
        print('                                            \x1b[38;2;255;255;255m─┼────┼────┼────┼────┼────┼────┼────┼────┤         \x1b[38;2;255;255;255m─┼────┼────┼────┼────┼────┼────┼────┼────┤') # prints the divider between rows
