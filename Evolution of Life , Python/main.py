import sys, tty
import os
import time
X,Y = 10,10
tty.setcbreak(sys.stdin)

def Grid(x, y):
    grid = []  # empty grid
    for i in range(y):  # generates row
        row = []
        for j in range(x):
            row.append(' ')  #appends row to list
        grid.append(row)
    #print(grid)
    return grid

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
board  = Grid(X,Y)

def usrInp():
    Input = [0, 0, 0]
    enterCheck = False
    delCheck  = False
    end = False
    keyTypes = [65, 66, 67, 68, 91, 27]
    for i in range(3):
        key = ord(sys.stdin.read(1))
        if key in keyTypes:
            if key not in Input:
                Input[i] = key

        else:
            if key == 10:
                enterCheck = True
            if key == 127:
                delCheck = True
            if key == 99:
                end = True
            break
    return [Input, enterCheck, delCheck, end]

def place(x,y,board):
    mainColor = ['\x1b[38;2;15;82;186m\u2588','\x1b[38;2;75;104;185m\u2588','\x1b[38;2;0;181;226m\u2588','\x1b[38;2;0;138;216m\u2588']
    board[y][x] =  mainColor[0]
    Temp = mainColor[0]
    return Temp
def delete(x,y,board):
    board[y][x] = ' '
    Temp = ' '
    return Temp

def mainP1(board): 
    x = 0
    y = 0

    NotPlaced = True
    
    
    temp = board[y][x]
    newTemp = ' '
    while NotPlaced:
        print(x + 1, y + 1)

        Display(board)
        inputs = usrInp()
        enterCheck = inputs[1]
        delCheck = inputs[2]
        end = inputs[3]
        Input = inputs[0]
        print(Input)
    

        if 67 in Input:

            x += 1
            if x == len(board):
                x = 0
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'
            board[y][x - 1] = temp
            Input = [0, 0, 0]
        if 68 in Input:

            x -= 1

            if x == -1:
                x = len(board)-1
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'

            if x == len(board)-1:
                board[y][0] = temp
            else:
                board[y][x + 1] = temp

            Input = [0, 0, 0]
        if 66 in Input:

            y += 1
            if y == len(board):
                y = 0
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'
            board[y - 1][x] = temp
            Input = [0, 0, 0]
        if 65 in Input:

            y -= 1
            if y == -1:
                y = len(board)-1
            newTemp = board[y][x]
            board[y][x] = '\x1b[38;2;255;255;255m\u2588'
            if y == len(board)-1:
                board[0][x] = temp
            else:
                board[y + 1][x] = temp
            Input = [0, 0, 0]
        if enterCheck == True:
            newTemp = place(x,y,board)
            Input = [0,0,0]
        if delCheck == True:
            newTemp = delete(x,y,board)
        os.system('clear')
        if end == True:
            NotPlaced = False
            Input = [0, 0, 0]
        

        temp = newTemp

        #print(temp)
    #print(board)
    return board
mainP1(board)


#print(board)

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

        try:
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
            else:
                n1 = board[x-1][y]
                n2 = board[x+1][y]

                n3  = board[x][y-1]
                n4  = board[x][y+1]

                n5 = board[x-1][y+1]
                n6 = board[x-1][y-1]
                n7 = board[x+1][y+1]
                n8 = board[x+1][y-1]
                
        except:
                pass
        
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

def stage3(Neighbours2,locs):
    cords = [ ]
    nCount = 1
    for i in locs:
        Nc = 0
        for j in Neighbours2[f'S{nCount}']:
            if j == '\x1b[38;2;15;82;186m█':
                Nc+=1
        if Nc == 3:
            cords.append(i)
        nCount+=1
    return cords

def NewGen(aCords,dCords,g):
    for i in aCords:
        x = i[0]
        y = i[1]
        g[x][y] = '\x1b[38;2;15;82;186m█'

    for j in dCords:
        x = j[0]
        y = j[1]
        g[x][y] = '\x1b[38;2;15;82;186m█'






def mainP2(board):
    
    Display(board)
    while True:
        g = Grid(X,Y)
        ALoc = aliveLocation(board)
        DLoc = deadLocation(board)
        DLocs  = DLoc[0]
        Locs = ALoc[0]
        count = ALoc[1]
        #for i in Locs:
            #print(i)
        #print(count)
        Neighbours  = stage1(Locs,board)
        Neighbours2 = stage1(DLocs,board)
        #print(Neighbours2)
        
        aliveCords = stage2(Neighbours,Locs)
        deadCords = stage3(Neighbours2,DLocs)
        NewGen(aliveCords,deadCords,g)
        Display(g)
        os.system('clear')
        board = g




mainP2(board)
