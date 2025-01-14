import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor
import time
import os
import random
import sys, tty

def boxCollision(display,  characterPos  , objectPos):

    #box collisions works on the idea that the 2 objects and their positions are not near each other
    #for example the x pos of object - character must not = 0
    #similarily this applies for the y pos 
    #to do this we add positional args for each edge of the objects and monitor each of the calulations
    x = characterPos[0]
    y = characterPos[1]
    '''characterBoxPos = [ [x+1,y+1],[x+1,y],[x+1,y-1],
                        [x-1,y+1],[x-1,y],[x-1,y-1],
                        [x,y+1],[x,y-1]]'''
    characterBoxPosTop = [[x+1,y+1],[x-1,y+1],[x,y+1]]
    characterBoxPosBottom = [[x+1,y-1],[x+1,y-1],[x,y-1]]
    characterBoxPosSide = [[x+1,y],[x-1,y]]
    x1 =  objectPos[0]
    y1 = objectPos[1]
    '''
    objectBoxPos = [ [x1+1,y1+1],[x1+1,y1],[x1+1,y1-1],
                        [x1-1,y1+1],[x1-1,y1],[x1-1,y1-1],
                        [x1,y1+1],[x1,y1-1]]'''
    objectBoxPosTop = [[x1+1,y1+1],[x1-1,y1+1],[x1,y1+1]]
    objectBoxPosBottom = [[x1+1,y1-1],[x1+1,y1-1],[x1,y1-1]]
    objectBoxPosSide = [[x1+1,y1],[x1-1,y1]]
    for i in range(3):
        #print(characterBoxPosBottom[i][1] - objectBoxPosTop[i][1] )
        if characterBoxPosBottom[i][1] - objectBoxPosTop[i][1] == -2 and (x1 == x or x1-1 == x or x1+1 == x or  x1-2 == x or x1+2 == x):
            return False
    if (objectBoxPosSide[1][0] - characterBoxPosSide[0][0] == 0) and characterBoxPosSide[0][1] == objectBoxPosSide[1][1]:
        return False

    
def addBoxColider(item,type):
    if type == 1:
        itemBox = [ [u'\u3164',u'\u3164',u'\u3164',u'\u3164',u'\u3164' ],
                [u'\u3164',' ',' ',' ',u'\u3164'],
                [u'\u3164',' ',' ',' ',u'\u3164'],
                [u'\u3164',' ',' ',' ',u'\u3164'],
                [u'\u3164',u'\u3164',u'\u3164',u'\u3164',u'\u3164']]
    if type == 2:
        itemBox = [ [u'\u3164',u'\u3164',u'\u3164',u'\u3164',u'\u3164' ],
                [u'\u3164',' ',' ',' ',u'\u3164'],
                [u'\u3164',' ',' ',' ',u'\u3164'],
                [u'\u3164',' ',' ',' ',u'\u3164']]
    row = 1
    column = 1
    for i in item:
        for j in i:
            if column == 4:
                column = 1
            if row < 4 and column < 4:
                itemBox[row][column] = j
        
            column += 1
        row +=1
    return itemBox