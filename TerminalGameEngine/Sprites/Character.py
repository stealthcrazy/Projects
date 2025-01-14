import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import os
import random
import sys, tty


def displayCharacter(display,pos,y1 = 5 ,y2 = 6,y3 = 7):
    i = pos
    character = [   ['|','‾‾‾','|  '],
                    ['|',' 0 ','|'],
                    ['|','___','|'],]
    character1 = [   [' ','0',' '],
                    ['-','|','-'],
                    [' ','^',' '],]

    display[y1][i] = character[0][0]
    display[y1][i+1] = character[0][1]
    display[y1][i+2] = character[0][2]
    display[y2][i+2] = character[1][2]
    display[y2][i+1] = character[1][1]
    display[y2][i] = character[1][0]
    display[y3][i] = character[2][0]
    display[y3][i+1] = character[2][1] 
    display[y3][i+2] = character[2][2]
             # removes previous chars
    '''
        display[y1][i-1] = ' '
        display[y1][i-2] = ' '
        display[y1][i-3] = ' '
        display[y2][i-1] = ' '
        display[y2][i-2] =  ' '
        display[y2][i-3] = ' '
        display[y3][i-1] = ' '
        display[y3][i-2] =  ' '
        display[y3][i-3] =  ' '
        '''

        

        
    
    return character