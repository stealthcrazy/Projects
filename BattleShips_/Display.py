import time
import os 
import sys ,tty
import asyncio
import threading
import random
from cfonts import render, say

def Display(board,wCount,sCount):
    row = 0
    output = render('Battle Ships', align='center',colors = ['blue','yellow'])
    print(output)
    print('\n')
    print('                                                                       A     B    C    D    E    F    G    H')
    for i in board:
        string = f'{row+1}|'
        counter = 0 
        for j in i:
            #if counter != len(i)-1:
                #string += ' '+j +'  \x1b[38;2;255;255;255m|'
            #else:
                #string += j
            string += ' '+j +'  \x1b[38;2;255;255;255m|'
            counter+=1
        print('                                                                    ',string)
        
        if row != len(board)-1:
            print('                                                                     \x1b[38;2;255;255;255m─┼────┼────┼────┼────┼────┼────┼────┼────┤')
            row +=1
        x = ''
    print('\n')
    print('                                                                                            ]+[           ','\n',
            '                                                                                          --|--          ','\n',      
            '                                                                                          |_|__|         ', '\n',           
            '                                                                                          |____|         ','\n',
            '                                                       ____________________________________|65|_______________________________','\n',
            '                                                         \                   \                        (______)               /','\n',
            '                                                       __~~~~~~~~~OOooo_______\__________________________________________~~~~ooo__')
    print(f'                                                        {wCount} left: Press W to select Warship')
    print('\n')

    print( ' ','\n',
            '                                                                                                     __|_|__                            ','\n',
            '                                                                                                    |  751  |                          ','\n',
            '                                                           __                    ___________________|       |_________________         ','\n',
            '                                                          |   -_______-----------                                              \       ','\n',
            '                                                         >|    _____                                                   --->     )      ','\n',
            '                                                          |__ -     ---------_________________________________________________ /')
    print(f'                                                       {sCount} left: Press S to select Submarine')
    


