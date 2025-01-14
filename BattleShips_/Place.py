from Overlap import *

def place(x,y,board,value,type,ship,axis,WarShipCount,SubmarineCount, current ):
    Temp = ' '
    mainColor = ['\x1b[38;2;15;82;186m\u2588','\x1b[38;2;75;104;185m\u2588','\x1b[38;2;0;181;226m\u2588','\x1b[38;2;0;138;216m\u2588']
    
    if type =='enter':
        Temp = current 
        if value == True:
            if ship == 'warship':
                overlap = checkOverlap(board,x,y,'warship')
                if axis == 'horizontal' and overlap == False and WarShipCount>0 :
                    if x+2<=7 and x+1<=7 and x-1 >=0:
                        board[y][x] =mainColor[0]
                        board[y][x+1] =mainColor[1]
                        board[y][x+2] =mainColor[1]
                        board[y][x-1] =mainColor[1]
                        WarShipCount -= 1
                        Temp = mainColor[0]

                        

                if axis == 'verticle'  and overlap == False and WarShipCount>0:
                    if y+2<=7 and y+1<=7 and y-1>=0:
                        board[y][x] =mainColor[0]
                        board[y+1][x] =mainColor[1]
                        board[y+2][x] =mainColor[1]
                        board[y-1][x] =mainColor[1]
                        WarShipCount -= 1
                        Temp = mainColor[0]
            if ship == 'submarine'  :
                overlap = checkOverlap(board,x,y,'submarine')
                if axis == 'horizontal'and overlap == False and SubmarineCount>0:
                    if  x+1<=7 and x-1 >=0:
                        board[y][x] =mainColor[2]
                        board[y][x+1] =mainColor[3]
                        board[y][x-1] =mainColor[3]
                        SubmarineCount -= 1
                        Temp = mainColor[2]
                if axis == 'verticle' and overlap == False  and SubmarineCount>0:
                    if y+1<=7 and y-1>=0:
                        board[y][x] =mainColor[2]
                        board[y+1][x] =mainColor[3]
                        board[y-1][x] =mainColor[3]
                        SubmarineCount -= 1
                        Temp = mainColor[2]
                
    if type =='del':
        if value == True:
            SubmarineColors = ['\x1b[38;2;0;181;226m\u2588','\x1b[38;2;0;138;216m\u2588']
            WarshipColors = ['\x1b[38;2;15;82;186m\u2588','\x1b[38;2;75;104;185m\u2588']
            Temp = current 
            try:
                if current == SubmarineColors[0] and board[y][x+1] in SubmarineColors and board[y][x-1] in SubmarineColors:
                        board[y][x] = ' '
                        board[y][x+1] = ' '
                        board[y][x-1] = ' '
                        SubmarineCount += 1
                        Temp = ' '
            except IndexError:
                pass
            try:
                if current == SubmarineColors[0] and board[y-1][x] in SubmarineColors and board[y+1][x] in SubmarineColors:
                        board[y][x] = ' '
                        board[y+1][x] =' '
                        board[y-1][x] =' '
                        SubmarineCount += 1
                        Temp = ' '
            except IndexError:
                pass
            try:
                if current ==  WarshipColors[0] and board[y-1][x] in WarshipColors and board[y+1][x] in WarshipColors:
                        board[y][x] = ' '
                        board[y+1][x] =' '
                        board[y+2][x] =' '
                        board[y-1][x] =' '
                        WarShipCount += 1
                        Temp = ' '
            except IndexError:
                pass
            try:
                if current ==  WarshipColors[0] and board[y][x+1] in WarshipColors and board[y][x-1] in WarshipColors:
                        board[y][x] = ' '
                        board[y][x+1] = ' '
                        board[y][x+2] = ' '
                        board[y][x-1] = ' '
                        WarShipCount += 1
                        Temp = ' '
            except IndexError:
                pass
         
            
    #print(WarShipCount,SubmarineCount)
    return [WarShipCount,SubmarineCount,Temp]