def checkOverlap(board,x,y,ship):
    types = ['\x1b[38;2;15;82;186m\u2588','\x1b[38;2;75;104;185m\u2588','\x1b[38;2;0;181;226m\u2588','\x1b[38;2;0;138;216m\u2588']
    checkOverlap= False
    if ship == 'warship':
        if x+2<= 7 and  y+2<=7:
            if board[y][x] in types or board[y+1][x] in types or  board[y-1][x] in types or board[y+2][x] in types  or board[y][x+2] in types  or board[y][x+1] in types or board[y][x-1] in types:
                checkOverlap = True
        elif x+1<= 7 and  y+1<=7:
            if board[y][x] in types or board[y+1][x] in types or  board[y-1][x] in types  or board[y][x+1] in types or board[y][x-1] in types:
                checkOverlap = True
        else:
            if board[y][x] in types or  board[y-1][x] in types  or board[y][x-1] in types:
                checkOverlap = True
    if ship == 'submarine':
        if x+1<= 7 and  y+1<=7:
            if board[y][x] in types or board[y+1][x] in types or  board[y-1][x] in types  or board[y][x+1] in types or board[y][x-1] in types:
                checkOverlap = True
        else:
            if board[y][x] in types or  board[y-1][x] in types  or board[y][x-1] in types:
                checkOverlap = True
        
    return checkOverlap