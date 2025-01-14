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
        #display[8][i] = '\x1b[38;2;0;0;255m\u2588'
        display[8][i] = '_'


    for i in range(len(display)):
        for j in range(len(display[i])):
            if j < len(display[i])-1 :
                print(display[i][j],end = '')
            else:
                 print(display[i][j],end = '\n')
    print(' ')
    print(' ')

def mapDisplay(display):
    map = []
    for i in range(len(display)):
        map.append([])
        for j in range(len(display[i])):
            map[i].append(j)