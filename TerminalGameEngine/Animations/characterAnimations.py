import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import os
import random
import sys, tty

def Display(display):
    print(' ')
    for i in range(len(display[8])):
        display[8][i] = '_'


    for i in range(len(display)):
        for j in range(len(display[i])):
            if j < len(display[i])-1 :
                print(display[i][j],end = '')
            else:
                 print(display[i][j],end = '\n')
    print(' ')
    print(' ')

'''
def characterJump(display,character,pos, y1 , y2 ,  y3 ):
    if y1 == 5 and y2 == 6 and y3 == 7:
        os.system('clear')
        for i in range(3):
            display[y1-i][pos] = character[0][0]
            display[y1-i][pos+1] = character[0][1]
            display[y1-i][pos+2] = character[0][2]
            display[y2-i][pos+2] = character[1][2]
            display[y2-i][pos+1] = character[1][1]
            display[y2-i][pos] = character[1][0]
            display[y3-i][pos] = character[2][0]
            display[y3-i][pos+1] = character[2][1]
            display[y3-i][pos+2] = character[2][2]
            display[y1][pos] = ' '
            display[y1][pos+1] = ' '
            display[y1][pos+2] = ' '
            display[y2][pos] = ' '
            display[y2][pos+1] =  ' '
            display[y2][pos+2] = ' '
            display[y3][pos] = ' '
            display[y3][pos+1] =  ' '
            display[y3][pos+2] =  ' '
            Display(display)
            time.sleep(0.09) 

                
            os.system('clear')
            
        
        y1 = y1-3
        y2 = y2-3
        y3 = y3-3
    return [y1,y2,y3]

'''
def characterJump(display,character,pos, y1 , y2 ,  y3 ):
    if y1 >= 2 and y2 >= 3 and y3 >= 4  :
        y1 = y1-1
        y2 = y2-1
        y3 = y3-1
    return [y1, y2 , y3]