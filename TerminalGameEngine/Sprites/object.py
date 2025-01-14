import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import os
import random
import sys, tty




def displayObject(display,pos):
    object = [  [' ','  ',' '],
                [' ','/\\',' '],
                ['/','  ','\\' ],]
    display[5][pos] = object[0][0]
    display[5][pos+1] = object[0][1]
    display[5][pos+2] = object[0][2]
    display[6][pos] = object[1][2]
    display[6][pos+1] = object[1][1]
    display[6][pos+2] = object[1][0]
    display[7][pos] = object[2][0]
    display[7][pos+1] = object[2][1]
    display[7][pos+2] = object[2][2]
    return object
def displayObjects(display):
    positions = []
    for i in range(random.randint(1,3)):
        position = random.randint(60,100)
        positions.append(position)
    object = [  [' ','  ',' '],
                [' ','/\\',' '],
                ['/','  ','\\' ],]
    for pos in positions:
        display[5][pos] = object[0][0]
        display[5][pos+1] = object[0][1]
        display[5][pos+2] = object[0][2]
        display[6][pos] = object[1][2]
        display[6][pos+1] = object[1][1]
        display[6][pos+2] = object[1][0]
        display[7][pos] = object[2][0]
        display[7][pos+1] = object[2][1]
        display[7][pos+2] = object[2][2]
    return object