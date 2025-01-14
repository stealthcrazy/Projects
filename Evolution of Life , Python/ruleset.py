import time
import os

def Display(board):
    row = 0
    print('\n')
    for i in board:  # displays grid for placing using for loop
        #string = f'{row+1}|'
        string = f' '
        counter = 0
        for j in i:
            #if counter != len(i)-1:
            #string += ' '+j +'  \x1b[38;2;255;255;255m|'
            #else:
            #string += j
            string += ' ' + j + ' \x1b[38;2;255;255;255m|'  #runs through list for each row
            counter += 1
        print(string)

        if row != len(board) - 1:
            print(')___'*len(board[0]))
            row += 1
        #x = ''
    print('\n')
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['\x1b[38;2;15;82;186m█', ' ', '\x1b[38;2;15;82;186m█', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '\x1b[38;2;15;82;186m█', ' ', ' ', ' ', '\x1b[38;2;15;82;186m█', ' '], [' ', ' ', '\x1b[38;2;15;82;186m█', ' ', ' ', ' ', ' ', '\x1b[38;2;15;82;186m█', ' ', ' '], [' ', ' ', '\x1b[38;2;15;82;186m█', ' ', ' ', ' ', '\x1b[38;2;15;82;186m█', '\x1b[38;2;15;82;186m█', '\x1b[38;2;15;82;186m█', ' '], [' ', ' ', ' ', '\x1b[38;2;15;82;186m█', '\x1b[38;2;15;82;186m█', ' ', ' ', ' ', ' ', ' '], [' ', ' ', '\x1b[38;2;15;82;186m█', ' ', ' ', ' ', '\x1b[38;2;15;82;186m█', '\x1b[38;2;15;82;186m█', ' ', ' '], ['\x1b[38;2;15;82;186m█', ' ', ' ', '\x1b[38;2;15;82;186m█', ' ', ' ', '\x1b[38;2;15;82;186m█', '\x1b[38;2;15;82;186m█', ' ', ' '], ['\x1b[38;2;15;82;186m█', '\x1b[38;2;15;82;186m█', ' ', '\x1b[38;2;15;82;186m█', '\x1b[38;2;15;82;186m█', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def Grid(x, y):
    grid = []  # empty grid
    for i in range(y):  # generates row
        row = []
        for j in range(x):
            row.append(' ')  #appends row to list
        grid.append(row)
    #print(grid)
    return grid


def aliveLocation(board):
    locs = []
    count = 0
    row = 0
    column = 0 
    for i in board:
        
        for j in i:
            if j == '\x1b[38;2;15;82;186m█':
                locs.append([row,column])
                count+=1
            column +=1
        column = 0
        row +=1
    return [locs,count]

def deadLocation(board):
    locs = []
    count = 0
    row = 0
    column = 0 
    for i in board:
        
        for j in i:
            if j == ' ':
                locs.append([row,column])
                count+=1
            column +=1
        column = 0
        row +=1
    return [locs,count]



def stage1(locs,board):
    LocNeighbours = {

    }
    count = 1
    for i in locs:
        
        Neighbours = []
        x = i[0]
        y = i[1]

        n1 = board[x-1][y]
        n2 = board[x+1][y]

        n3  = board[x][y-1]
        n4  = board[x][y+1]

        n5 = board[x-1][y+1]
        n6 = board[x-1][y-1]
        n7 = board[x+1][y+1]
        n8 = board[x+1][y-1]
        if x+1 == len(board) :
            n1 = board[x-1][y]
            

            n3  = board[x][y-1]
            n4  = board[x][y+1]

            n5 = board[x-1][y+1]
            n6 = board[x-1][y-1]
            
            
            n2 = None
            n7 = None
            n8 = None

        if x-1 == -1 :
            
            n2 = board[x+1][y]

            n3  = board[x][y-1]
            n4  = board[x][y+1]

            n7 = board[x+1][y+1]
            n8 = board[x+1][y-1]

            n1 = None
            n5 = None
            n6 = None
        if y+1 == len(board) :
            n1 = board[x-1][y]
            n2 = board[x+1][y]

            n3  = board[x][y-1]

            n6 = board[x-1][y-1]
            n8 = board[x+1][y-1]


            n4  = None
            n7 = None
            n5 = None
        if y-1 == -1 :
            n1 = board[x-1][y]
            n2 = board[x+1][y]
            n4  = board[x][y+1]

            n5 = board[x-1][y+1]
            
            n7 = board[x+1][y+1]
            

            n3  = None
            n6 = None
            n8 = None
            

        
        Neighbours.append(n1)
        Neighbours.append(n2)
        Neighbours.append(n3)
        Neighbours.append(n4)
        Neighbours.append(n5)
        Neighbours.append(n6)
        Neighbours.append(n7)
        Neighbours.append(n8)
        LocNeighbours[f'S{count}'] = Neighbours
        count+=1
    return LocNeighbours
def stage2(Neighbours,locs):
    cords = [ ]
    nCount = 1
    for i in locs:
        Nc = 0
        for j in Neighbours[f'S{nCount}']:
            if j == '\x1b[38;2;15;82;186m█':
                Nc+=1
        if Nc == 3 or Nc ==2:
            cords.append(i)
        nCount+=1
    return cords

def stage3(Neighbours,locs):
    cords = [ ]
    nCount = 1
    for i in locs:
        Nc = 0
        for j in Neighbours[f'S{nCount}']:
            if j == ' ':
                Nc+=1
        if Nc == 3 or Nc ==2:
            cords.append(i)
        nCount+=1
    return cords

def NewGen(aCords,dCords,g):
    for i in aCords:
        x = i[0]
        y = i[1]
        g[y][x] = '\x1b[38;2;15;82;186m█'
    for j in dCords:
        x = j[0]
        y = j[1]
        g[y][x] = '\x1b[38;2;15;82;186m█'






def mainP2(board):
    
    Display(board)
    for i in range(100):
        g = Grid(10,10)
        ALoc = aliveLocation(board)
        DLoc = aliveLocation(board)
        DLocs  = DLoc[0]
        Locs = ALoc[0]
        count = ALoc[1]
        #for i in Locs:
            #print(i)
        #print(count)
        Neighbours  = stage1(Locs,board)
        Neighbours2 = stage1(DLocs,board)
        #print(Neighbours)
        
        aliveCords = stage2(Neighbours,Locs)
        deadCords = stage3(Neighbours,Locs)
        NewGen(aliveCords,deadCords,g)
        Display(g)
        time.sleep(0.1)
        os.system('clear')




mainP2(board)