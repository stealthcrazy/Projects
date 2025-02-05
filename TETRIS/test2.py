import os
import time
import sys, tty
import random
import threading
import subprocess
from screen import Screen


NotOver = True
Inp = None
INP = [0, 0, 0]
MENU = True


def genGrid(x, y):
    grid = []
    for i in range(y):
        row = []
        seq = genSequence(22)
        for j in range(x):
            if i == 0 or i == 1:
                row.append(
                    " "
                    + "\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588"
                    + " "
                )
            if i == y - 2 or i == y - 1:
                row.append(
                    " "
                    + "\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588"
                    + " "
                )

            if (i != 0 and i != 1 and i != y - 2 and i != y - 1) and (
                j == 0 or j == 11
            ):
                if i not in seq:
                    row.append(
                        " "
                        + "\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588\x1b[38;2;119;119;119m\u2588"
                        + " "
                    )
            if (i != 0 and i != 1 and i != y - 2 and i != y - 1) and (
                j != 0 and j != 11
            ):
                if i not in seq:
                    # row.append(" \x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588 ")
                    row.append("      ")

        grid.append(row)
    return grid


def genSequence(x):
    seq = []
    for i in range(1, x):
        # print(i)
        seq.append((i * 3) - 1)
    return seq


# print(genSequence(22))
def Grid(x, y):
    grid = []
    for i in range(y):
        row = []
        for j in range(x):
            row.append(" ")
        grid.append(row)
    # print(grid)
    return grid


def displayGrid(grid):
    # width = os.get_terminal_size().columns
    for i in grid:
        row = " " * (int(os.get_terminal_size().columns / 2) - 40)
        for j in i:
            row += j
        print(row)


def dropTest(Dgrid, Tet, x, y=1):

    Dgrid[x][y] = Tet[0]
    Dgrid[x + 1][y] = Tet[1]


def usrInp():
    global NotOver
    global INP
    global MENU

    keyTypes = [65, 66, 67, 68, 91, 27]
    while NotOver and (not MENU):
        for i in range(3):
            if NotOver == False:
                break
            key = ord(sys.stdin.read(1))
            if key in keyTypes:
                if key not in INP:
                    INP[i] = key

        # print(INP)


def Input():
    global NotOver
    global Inp
    while NotOver:

        key = ord(sys.stdin.read(1))
        print(key)
        Inp = key


def linkRenders(DISPLAY_GRID_FRONT_, DISPLAY_GRID_BACK_):
    for i in range(len(DISPLAY_GRID_FRONT_)):
        for j in range(len(DISPLAY_GRID_FRONT_[0])):
            try:
                DISPLAY_GRID_BACK_[i][j] = DISPLAY_GRID_FRONT_[i][j]
            except IndexError:
                pass
    return DISPLAY_GRID_BACK_


def Spawn(TetType):
    Cx = random.randint(0, 9)
    if TetType == "TETROMINO_I":
        Cx = random.randint(1, 7)
    if TetType == "TETROMINO_O":
        Cx = random.randint(0, 8)
    if TetType == "TETROMINO_T":
        Cx = random.randint(1, 8)
    if TetType == "TETROMINO_J":
        Cx = random.randint(1, 9)
    if TetType == "TETROMINO_L":
        Cx = random.randint(0, 8)
    if TetType == "TETROMINO_S":
        Cx = random.randint(1, 7)
    if TetType == "TETROMINO_Z":
        Cx = random.randint(1, 7)

    return Cx


def ProccessInputs(TetType, INPUT_, Cx, Cy, R, collisions, GRID_):
    """
    WASD

    L
    119
    97
    115
    100

    U
    87
    65
    83
    68
    """
    ColL = collisions[1]
    ColR = collisions[0]

    if TetType == "SINGLE_BLOCK":

        if (Cx > 0) or (Cx < 9):
            # print(Cx)
            if ColL == False:
                if sideblockCollider(GRID_, TetType, Cx - 1, Cy, R, "L") == False:

                    if INPUT_ == 68:
                        Cx -= 1
            if ColR == False:
                if sideblockCollider(GRID_, TetType, Cx + 1, Cy, R, "R") == False:

                    if INPUT_ == 67:
                        Cx += 1
            """
            if (INPUT_ == 97) or (INPUT_ == 65):
                        Cx-=1
            if (INPUT_ == 100) or (INPUT_ == 68):
                        Cx+=1
            """
    if TetType == "TETROMINO_I":

        # print(Cx)
        if ColL == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "L") == False:
                if INPUT_ == 68:
                    Cx -= 1

        if ColR == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "R") == False:

                if INPUT_ == 67:
                    Cx += 1

        """
            if (INPUT_ == 97) or (INPUT_ == 65):
                        Cx-=1
            if (INPUT_ == 100) or (INPUT_ == 68):
                        Cx+=1
            
            """
    if TetType == "TETROMINO_O":

        # print(Cx)
        if ColL == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "L") == False:
                if INPUT_ == 68:
                    Cx -= 1

        if ColR == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "R") == False:

                if INPUT_ == 67:
                    Cx += 1
    if TetType == "TETROMINO_T":

        # print(Cx)
        if ColL == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "L") == False:
                if INPUT_ == 68:
                    Cx -= 1

        if ColR == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "R") == False:

                if INPUT_ == 67:
                    Cx += 1
    if TetType == "TETROMINO_J":

        # print(Cx)
        if ColL == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "L") == False:
                if INPUT_ == 68:
                    Cx -= 1

        if ColR == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "R") == False:

                if INPUT_ == 67:
                    Cx += 1
    if TetType == "TETROMINO_L":

        # print(Cx)
        if ColL == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "L") == False:
                if INPUT_ == 68:
                    Cx -= 1

        if ColR == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "R") == False:

                if INPUT_ == 67:
                    Cx += 1
    if TetType == "TETROMINO_S":

        # print(Cx)
        if ColL == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "L") == False:
                if INPUT_ == 68:
                    Cx -= 1

        if ColR == False:
            if sideblockCollider(GRID_, TetType, Cx, Cy, R, "R") == False:

                if INPUT_ == 67:
                    Cx += 1
    if TetType == "TETROMINO_Z":

        # print(Cx)
        if ColL == False:
            if sideblockCollider(GRID_, TetType, Cx - 1, Cy, R, "L") == False:
                if INPUT_ == 68:
                    Cx -= 1

        if ColR == False:
            if sideblockCollider(GRID_, TetType, Cx + 1, Cy, R, "R") == False:

                if INPUT_ == 67:
                    Cx += 1

        """
            if (INPUT_ == 97) or (INPUT_ == 65):
                        Cx-=1
            if (INPUT_ == 100) or (INPUT_ == 68):
                        Cx+=1
            """
    return Cx


def GameOver(GRID__):

    over = False
    for i in GRID__[0]:
        if i[0] == "P":
            over = True
            break

    return over


def Redisplay(grid):
    DISPLAY_GRID_FRESH = genGrid(12, 65)
    displayReLink(grid, DISPLAY_GRID_FRESH)
    return DISPLAY_GRID_FRESH


def displayGame():
    GRID_ = Grid(10, 20)
    DISPLAY_GRID_FRONT = genGrid(12, 65)
    DISPLAY_GRID_BACK = genGrid(12, 65)
    displayGrid((DISPLAY_GRID_FRONT))
    time.sleep(0.1)
    os.system("clear")
    colliding = False
    global NotOver
    global INP
    global MENU
    Tetronminos = [
        "TETROMINO_I",
        "TETROMINO_O",
        "TETROMINO_T",
        "TETROMINO_J",
        "TETROMINO_L",
        "TETROMINO_S",
        "TETROMINO_Z",
    ]
    # speed = 10
    # Tetronminos = ["TETROMINO_L",]
    while NotOver and (not MENU):

        TetType_ = random.choice(Tetronminos)
        # TetType_ = "SINGLE_BLOCK"
        Cx = Spawn(TetType_)

        R = 0
        for i in range(20):

            if colliding == False:
                print(TetType_)

                boundryCollision = BoundryCollider(
                    TetType_,
                    Cx,
                    i,
                    R,
                )

                if INP[2] == 66 and i > 1:

                    Rcollision = rotationCollider(TetType_, Cx, i, R, GRID_)
                    rLock = RotationProccessing(TetType_, Cx, R, boundryCollision)
                    print(rLock)
                    if Rcollision == False and rLock == False:
                        R += 90
                        if R == 360:
                            R = 0

                Cx = ProccessInputs(TetType_, INP[2], Cx, i, R, boundryCollision, GRID_)
                # print(f"R: {R}")
                # print(Cx)

                INP = [0, 0, 0]
                displayMapRefresh(GRID_)
                colliding = BoxCollider(TetType_, Cx, i, R, GRID_)

                displayMap(TetType_, Cx, i, R, GRID_)
                displayLink(GRID_, DISPLAY_GRID_BACK, TetType_)

                # DisplayMapTest(GRID_)
                displayGrid(DISPLAY_GRID_BACK)
                if (i != 19) and (colliding == False):
                    DISPLAY_GRID_BACK = linkRenders(
                        DISPLAY_GRID_FRONT, DISPLAY_GRID_BACK
                    )

                time.sleep(0.1)
                os.system("clear")
        SolidifyTetrominos(GRID_)

        result = delFullTetrominoRow(GRID_)
        Flag = result[0]
        result = delFullTetrominoRow(GRID_)
        GRID_ = result[1]
        SolidifyTetrominos(GRID_)

        # print(Flag)

        if Flag == True:

            DISPLAY_GRID_BACK = Redisplay(GRID_)

            # time.sleep(10)

        # DisplayMapTest(GRID_)
        if Flag == False:
            displayLink(GRID_, DISPLAY_GRID_BACK, TetType_)

        displayGrid((DISPLAY_GRID_BACK))
        time.sleep(0.1)

        os.system("clear")
        DISPLAY_GRID_FRONT = linkRenders(DISPLAY_GRID_BACK, DISPLAY_GRID_FRONT)
        colliding = False
        NotOver = not GameOver(GRID_)

    """
    colliding = False  
    for i in range(20):
        if colliding == False:
            displayMapRefresh(GRID_)
            colliding = BoxCollider("TETROMINO_O",1,i,0,GRID_)
            displayMap("TETROMINO_O",1,i,0,GRID_)  
            displayLink(GRID_,DISPLAY_GRID_,None)
            #DisplayMapTest(GRID_)
            time.sleep(0.1)
            os.system('clear')
        
    SolidifyTetrominos(GRID_)   """

    """
    TetrominoA = [' \x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588 ',
                    ' \x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588\x1b[38;2;255;0;0m\u2588 ']
    TetrominoB = [' \x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588 ',
                    ' \x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588 ']
    DISPLAY_GRID_ =genGrid(12,65)
    displayGrid((DISPLAY_GRID_))
    dropTest(DISPLAY_GRID_,TetrominoA,3)
    os.system('clear')
    time.sleep(0.01)
    displayGrid((DISPLAY_GRID_))
    j = 1
    
    for i in range(2,21):

        rmBlock(DISPLAY_GRID_,j*3)
        dropTest(DISPLAY_GRID_,TetrominoA,3*i)
        rmBlock(DISPLAY_GRID_,j*3,2)
        dropTest(DISPLAY_GRID_,TetrominoA,3*i,2)
        rmBlock(DISPLAY_GRID_,j*3,3)
        dropTest(DISPLAY_GRID_,TetrominoA,3*i,3)
        time.sleep(0.09)
        os.system('clear')
        displayGrid((DISPLAY_GRID_))
        j+=1
    j = 1
    l =1
    for i in range(2,20):
        key = Input()
        if key == 68:
            l+=1
        if key == 65:
            l-=1
        rmBlock(DISPLAY_GRID_,j*3,l)
        dropTest(DISPLAY_GRID_,TetrominoB,3*i,l)
        rmBlock(DISPLAY_GRID_,j*3,2)
        dropTest(DISPLAY_GRID_,TetrominoB,3*i,l+1)
        rmBlock(DISPLAY_GRID_,j*3,3)
        dropTest(DISPLAY_GRID_,TetrominoB,3*i,l+2)
        time.sleep(0.09)
        os.system('clear')
        
        displayGrid((DISPLAY_GRID_))
        j+=1
    """


def displayMapRefresh(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] == "B":
                grid[i][j] = " "


def displayMap(TetType, Cx, Cy, R, grid):

    try:
        if TetType == "SINGLE_BLOCK":
            grid[Cy][Cx] = "Bs"
        if TetType == "TETROMINO_I":  # Cx cant == 0 , 9,10
            if R == 0:
                grid[Cy][Cx] = "Bi"
                grid[Cy][Cx + 1] = "Bi"
                grid[Cy][Cx + 2] = "Bi"
                grid[Cy][Cx - 1] = "Bi"
            if R == 90:
                grid[Cy][Cx] = "Bi"
                grid[Cy + 1][Cx] = "Bi"
                grid[Cy + 2][Cx] = "Bi"
                grid[Cy - 1][Cx] = "Bi"
            if R == 180:
                grid[Cy][Cx] = "Bi"
                grid[Cy][Cx - 1] = "Bi"
                grid[Cy][Cx - 2] = "Bi"
                grid[Cy][Cx + 1] = "Bi"
            if R == 270:
                grid[Cy][Cx] = "Bi"
                grid[Cy - 1][Cx] = "Bi"
                grid[Cy - 2][Cx] = "Bi"
                grid[Cy + 1][Cx] = "Bi"

        if TetType == "TETROMINO_O":  # cx can't == 10 Cy cant == 20
            grid[Cy][Cx] = "Bo"
            grid[Cy][Cx + 1] = "Bo"
            grid[Cy + 1][Cx] = "Bo"
            grid[Cy + 1][Cx + 1] = "Bo"
        if TetType == "TETROMINO_T":
            if R == 0:
                grid[Cy][Cx] = "Bt"
                grid[Cy + 1][Cx] = "Bt"
                grid[Cy][Cx - 1] = "Bt"
                grid[Cy][Cx + 1] = "Bt"
            if R == 90:
                grid[Cy][Cx] = "Bt"
                grid[Cy][Cx - 1] = "Bt"
                grid[Cy - 1][Cx] = "Bt"
                grid[Cy + 1][Cx] = "Bt"
            if R == 180:
                grid[Cy][Cx] = "Bt"
                grid[Cy - 1][Cx] = "Bt"
                grid[Cy][Cx - 1] = "Bt"
                grid[Cy][Cx + 1] = "Bt"

            if R == 270:
                grid[Cy][Cx] = "Bt"
                grid[Cy][Cx + 1] = "Bt"
                grid[Cy + 1][Cx] = "Bt"
                grid[Cy - 1][Cx] = "Bt"
        if TetType == "TETROMINO_J":
            if R == 0:
                grid[Cy][Cx] = "Bj"
                grid[Cy + 1][Cx] = "Bj"
                grid[Cy + 2][Cx] = "Bj"
                grid[Cy + 2][Cx - 1] = "Bj"
            if R == 90:
                grid[Cy][Cx] = "Bj"
                grid[Cy][Cx - 1] = "Bj"
                grid[Cy][Cx - 2] = "Bj"
                grid[Cy - 1][Cx - 2] = "Bj"
            if R == 180:
                grid[Cy][Cx] = "Bj"
                grid[Cy - 1][Cx] = "Bj"
                grid[Cy - 2][Cx] = "Bj"
                grid[Cy - 2][Cx + 1] = "Bj"
            if R == 270:
                grid[Cy][Cx] = "Bj"
                grid[Cy][Cx + 1] = "Bj"
                grid[Cy][Cx + 2] = "Bj"
                grid[Cy - 1][Cx + 2] = "Bj"
        if TetType == "TETROMINO_L":

            if R == 0:
                grid[Cy][Cx] = "Bl"
                grid[Cy + 1][Cx] = "Bl"
                grid[Cy + 2][Cx] = "Bl"
                grid[Cy + 2][Cx + 1] = "Bl"
            if R == 90:
                grid[Cy][Cx] = "Bl"
                grid[Cy][Cx - 1] = "Bl"
                grid[Cy][Cx - 2] = "Bl"
                grid[Cy + 1][Cx - 2] = "Bl"
            if R == 180:
                grid[Cy][Cx] = "Bl"
                grid[Cy - 1][Cx] = "Bl"
                grid[Cy - 2][Cx] = "Bl"
                grid[Cy - 2][Cx - 1] = "Bl"
            if R == 270:
                grid[Cy][Cx] = "Bl"
                grid[Cy][Cx + 1] = "Bl"
                grid[Cy][Cx + 2] = "Bl"
                grid[Cy - 1][Cx + 2] = "Bl"
        if TetType == "TETROMINO_S":
            if R == 0 or R == 180:
                grid[Cy][Cx] = "Bs"
                grid[Cy + 1][Cx] = "Bs"
                grid[Cy + 1][Cx - 1] = "Bs"
                grid[Cy][Cx + 1] = "Bs"
            if R == 90 or R == 270:
                grid[Cy][Cx] = "Bs"
                grid[Cy][Cx - 1] = "Bs"
                grid[Cy - 1][Cx - 1] = "Bs"
                grid[Cy + 1][Cx] = "Bs"

        if TetType == "TETROMINO_Z":
            if R == 0 or R == 180:
                grid[Cy][Cx] = "Bz"
                grid[Cy + 1][Cx] = "Bz"
                grid[Cy + 1][Cx + 1] = "Bz"
                grid[Cy][Cx - 1] = "Bz"
            if R == 90 or R == 270:
                grid[Cy][Cx] = "Bz"
                grid[Cy - 1][Cx] = "Bz"
                grid[Cy + 1][Cx - 1] = "Bz"
                grid[Cy][Cx - 1] = "Bz"

    except IndexError:
        pass


def DisplayMapTest(grid):
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            row += "  |  " + grid[i][j] + "  |  "
        print(row)


# GRID_[18][2] = 'P'


def SolidifyTetrominos(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            try:
                btype = grid[i][j][1]
            except:
                pass

            if grid[i][j][0] == "B":
                grid[i][j] = f"P{btype}"


def pushTet(grid):
    notFallen = True
    while notFallen:
        for i in range(20):
            for j in range(10):
                if grid[i][j][0] == "P":
                    try:
                        if grid[i + 1][j] == " ":
                            notFallen = True
                            break
                        if grid[i + 1][j] != " ":
                            notFallen = False
                            break
                    except IndexError:
                        pass
        for i in range(20):
            for j in range(10):
                if grid[i][j][0] == "P":
                    try:
                        if grid[i + 1][j] == " ":

                            grid[i + 1][j] = grid[i][j]
                    except IndexError:
                        pass


def delFullTetrominoRow(grid):
    g = grid
    count = 0
    flag = False
    rowNum = 1
    blank = 1
    c = 0
    for i in range(1, len(grid)):

        for j in range(len(grid[0])):
            if grid[i][j][0] == "P":
                count += 1
        if count == len(grid[0]):
            flag = True
            break
        else:
            count = 0
        rowNum += 1
    if flag == True:
        g = [
            [
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
            ]
        ]

        for i in range(20):
            if i != rowNum:
                g.append(grid[i])

    return flag, g


"""
if TetType == "SINGLE_BLOCK":
            if grid[Cy][Cx+1] == 'P':
                collisionR = True
            if grid[Cy][Cx-1] == 'P':
                collisionL = True

if TetType == 'TETROMINO_I':# Cx cant == 0 , 9,10
            if grid[Cy][Cx+1] == 'P' or grid[Cy][Cx+2] == 'P' or grid[Cy][Cx+3] == 'P' or grid[Cy][Cx] == 'P':
                collisionR = True
            if grid[Cy][Cx-1] == 'P' or grid[Cy][Cx+1] == 'P' or grid[Cy][Cx+2] == 'P' or grid[Cy][Cx-2] == 'P':
                collisionL = True
            
            
            
        if TetType == 'TETROMINO_O': # cx can't == 10 Cy cant == 20
            if grid[Cy][Cx+1] == 'P' or grid[Cy][Cx+2] == 'P' or grid[Cy+1][Cx+1] == 'P' or grid[Cy+1][Cx+2] == 'P':
                collisionR = True
            if grid[Cy][Cx-1] == 'P' or grid[Cy][Cx] == 'P' or grid[Cy+1][Cx-1] == 'P' or grid[Cy+1][Cx] == 'P':
                collisionL = True
"""


def sideblockCollider(grid, TetType, Cx, Cy, R, Direction):

    try:
        if Direction == "R":
            blocks = getBlocks(TetType, Cx + 1, Cy, R, grid)
            for i in blocks:
                # print(i[0] == 'P')
                if i[0] == "P":

                    return True

        if Direction == "L":
            blocks = getBlocks(TetType, Cx - 1, Cy, R, grid)
            for i in blocks:
                # print(i[0] == 'P')
                if i[0] == "P":

                    return True

    except IndexError:
        print("error")

        pass
    return False


def sideblockCollidero(grid, TetType, Cx, Cy, R, Direction):
    collisionL = False
    collisionR = False
    try:
        if TetType == "SINGLE_BLOCK":
            if grid[Cy][Cx + 1][0] == "P":
                collisionR = True
            if grid[Cy][Cx - 1][0] == "P":
                collisionL = True

        if TetType == "TETROMINO_I":  # Cx cant == 0 , 9,10
            if R == 0:
                if grid[Cy][Cx + 2][0] == "P":
                    collisionR = True
                if grid[Cy][Cx - 1][0] == "P":
                    collisionL = True

        if TetType == "TETROMINO_O":  # cx can't == 10 Cy cant == 20
            if grid[Cy][Cx + 1][0] == "P" or grid[Cy + 1][Cx + 1][0] == "P":
                collisionR = True
            if grid[Cy][Cx][0] == "P" or grid[Cy + 1][Cx][0] == "P":
                collisionL = True
        if TetType == "TETROMINO_T":
            if grid[Cy][Cx + 1][0] == "P" or grid[Cy + 1][Cx][0] == "P":
                collisionR = True
            if grid[Cy][Cx - 1][0] == "P" or grid[Cy + 1][Cx][0] == "P":
                collisionL = True
        if TetType == "TETROMINO_J":
            if (
                grid[Cy][Cx][0] == "P"
                or grid[Cy + 1][Cx][0] == "P"
                or grid[Cy + 2][Cx][0] == "P"
            ):
                collisionR = True
            if (
                grid[Cy][Cx][0] == "P"
                or grid[Cy + 1][Cx][0] == "P"
                or grid[Cy + 2][Cx - 1][0] == "P"
            ):
                collisionL = True
        if TetType == "TETROMINO_L":
            if (
                grid[Cy][Cx][0] == "P"
                or grid[Cy + 1][Cx][0] == "P"
                or grid[Cy + 2][Cx + 1][0] == "P"
            ):
                collisionR = True
            if (
                grid[Cy][Cx][0] == "P"
                or grid[Cy + 1][Cx][0] == "P"
                or grid[Cy + 2][Cx][0] == "P"
            ):
                collisionL = True
        if TetType == "TETROMINO_S":
            if grid[Cy][Cx + 1][0] == "P" or grid[Cy + 1][Cx][0] == "P":
                collisionR = True
            if grid[Cy][Cx][0] == "P" or grid[Cy + 1][Cx - 1][0] == "P":
                collisionL = True
        if TetType == "TETROMINO_Z":
            if grid[Cy + 1][Cx + 1][0] == "P" or grid[Cy][Cx][0] == "P":
                collisionR = True
            if grid[Cy][Cx - 1][0] == "P" or grid[Cy + 1][Cx][0] == "P":
                collisionL = True

    except IndexError:
        pass

    # print([collisionL,collisionR])
    if Direction == "R":
        return collisionR
    if Direction == "L":
        return collisionL


def RotationProccessing(TetType, Cx, R, collisions):
    colR = collisions[0]
    colL = collisions[1]
    rotationLock = False
    if TetType == "TETROMINO_I":

        if R == 90 or R == 270:
            if colR == True:
                rotationLock = True
            if colL == True:
                rotationLock = True

    if TetType == "TETROMINO_O":

        pass
    if TetType == "TETROMINO_T":

        if R == 90:
            if colR == True:
                rotationLock = True
            if colL == True:
                rotationLock = True
        if R == 270:
            if colR == True:
                rotationLock = True
            if colL == True:
                rotationLock = True

    if TetType == "TETROMINO_J":
        if R == 0:

            if colL == True:
                rotationLock = True

        if R == 180:
            if colR == True:
                rotationLock = True
        if R == 270:
            if colR == True:
                rotationLock = True

    if TetType == "TETROMINO_L":
        if R == 0 or R == 90:

            if colL == True:
                rotationLock = True

        if R == 180:
            if colR == True:
                rotationLock = True
        if R == 90:
            if colL == True:
                rotationLock = True
    if TetType == "TETROMINO_S":
        pass

    if TetType == "TETROMINO_Z":
        pass
    return rotationLock


def BoundryCollider(
    TetType,
    Cx,
    Cy,
    R,
):
    collisionL = False
    collisionR = False
    if TetType == "SINGLE_BLOCK":

        if Cx == 0:  # define which boundry side
            collisionL = True
        if Cx == 9:
            collisionR = True
    if TetType == "TETROMINO_I":

        if R == 0:
            if Cx == 7:
                collisionR = True
            if Cx == 1:
                collisionL = True
        if R == 90 or R == 270:

            if Cx == 9:
                # print("hi")
                collisionR = True
            if Cx == 0:
                collisionL = True
        if R == 180:
            if Cx == 8:
                collisionR = True
            if Cx == 2:
                collisionL = True

    if TetType == "TETROMINO_O":

        if Cx == 8:
            collisionR = True
        if Cx == 0:
            collisionL = True
    if TetType == "TETROMINO_T":
        if R == 0 or R == 180:
            if Cx == 8:
                collisionR = True
            if Cx == 1:
                collisionL = True
        if R == 90:
            if Cx == 9:
                print("true")
                collisionR = True
            if Cx == 1:
                collisionL = True
        if R == 270:
            if Cx == 8:
                collisionR = True
            if Cx == 0:
                collisionL = True

    if TetType == "TETROMINO_J":
        if R == 0:
            if Cx == 9:
                collisionR = True
            if Cx == 1:
                collisionL = True
        if R == 90:
            if Cx == 9:
                collisionR = True
            if Cx == 2:
                collisionL = True
        if R == 180:
            if Cx == 8:
                collisionR = True
            if Cx == 0:
                collisionL = True
        if R == 270:
            if Cx == 7:
                collisionR = True
            if Cx == 0:
                collisionL = True

    if TetType == "TETROMINO_L":
        if R == 0:
            if Cx == 8:
                collisionR = True
            if Cx == 0:
                collisionL = True
        if R == 90:
            if Cx == 9:
                collisionR = True
            if Cx == 2:
                collisionL = True
        if R == 180:
            if Cx == 9:
                collisionR = True
            if Cx == 1:
                collisionL = True
        if R == 270:
            if Cx == 7:
                collisionR = True
            if Cx == 0:
                collisionL = True
    if TetType == "TETROMINO_S":
        if R == 0 or R == 180:
            if Cx == 8:
                collisionR = True
            if Cx == 1:
                collisionL = True
        if R == 90 or R == 270:
            if Cx == 9:
                collisionR = True
            if Cx == 1:
                collisionL = True

    if TetType == "TETROMINO_Z":
        """
        if  (Cx == 8):
            collisionR= True
        if (Cx == 1):
            collisionL = True
        """

        if R == 0 or R == 180:
            if Cx == 8:
                collisionR = True
            if Cx == 1:
                collisionL = True
        if R == 90 or R == 270:
            if Cx == 9:
                collisionR = True
            if Cx == 1:
                collisionL = True
    # print(collisionR,collisionL)
    return [collisionR, collisionL]


def getBlocks(TetType, Cx, Cy, R, grid):
    blocks = []

    if TetType == "TETROMINO_I":  # Cx cant == 0 , 9,10
        if R == 0:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx + 1],
                grid[Cy][Cx + 2],
                grid[Cy][Cx - 1],
            ]

        if R == 90:
            blocks = [
                grid[Cy][Cx],
                grid[Cy + 1][Cx],
                grid[Cy + 2][Cx],
                grid[Cy - 1][Cx],
            ]
        if R == 180:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx - 1],
                grid[Cy][Cx - 2],
                grid[Cy][Cx + 1],
            ]
        if R == 270:
            blocks = [
                grid[Cy][Cx],
                grid[Cy - 1][Cx],
                grid[Cy - 2][Cx],
                grid[Cy + 1][Cx],
            ]

    if TetType == "TETROMINO_O":  # cx can't == 10 Cy cant == 20
        blocks = [
            grid[Cy][Cx],
            grid[Cy][Cx + 1],
            grid[Cy + 1][Cx],
            grid[Cy + 1][Cx + 1],
        ]
    if TetType == "TETROMINO_T":
        if R == 0:
            blocks = [
                grid[Cy][Cx],
                grid[Cy + 1][Cx],
                grid[Cy][Cx - 1],
                grid[Cy][Cx + 1],
            ]
        if R == 90:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx - 1],
                grid[Cy - 1][Cx],
                grid[Cy + 1][Cx],
            ]
        if R == 180:
            blocks = [
                grid[Cy][Cx],
                grid[Cy - 1][Cx],
                grid[Cy][Cx - 1],
                grid[Cy][Cx + 1],
            ]

        if R == 270:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx + 1],
                grid[Cy + 1][Cx],
                grid[Cy - 1][Cx],
            ]
    if TetType == "TETROMINO_J":
        if R == 0:
            blocks = [
                grid[Cy][Cx],
                grid[Cy + 1][Cx],
                grid[Cy + 2][Cx],
                grid[Cy + 2][Cx - 1],
            ]
        if R == 90:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx - 1],
                grid[Cy][Cx - 2],
                grid[Cy - 1][Cx - 2],
            ]
        if R == 180:
            blocks = [
                grid[Cy][Cx],
                grid[Cy - 1][Cx],
                grid[Cy - 2][Cx],
                grid[Cy - 2][Cx + 1],
            ]
        if R == 270:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx + 1],
                grid[Cy][Cx + 2],
                grid[Cy - 1][Cx + 2],
            ]
    if TetType == "TETROMINO_L":

        if R == 0:
            blocks = [
                grid[Cy][Cx],
                grid[Cy + 1][Cx],
                grid[Cy + 2][Cx],
                grid[Cy + 2][Cx + 1],
            ]
        if R == 90:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx - 1],
                grid[Cy][Cx - 2],
                grid[Cy + 1][Cx - 2],
            ]
        if R == 180:
            blocks = [
                grid[Cy][Cx],
                grid[Cy - 1][Cx],
                grid[Cy - 2][Cx],
                grid[Cy - 2][Cx - 1],
            ]
        if R == 270:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx + 1],
                grid[Cy][Cx + 2],
                grid[Cy + 1][Cx + 2],
            ]
    if TetType == "TETROMINO_S":
        if R == 0 or R == 180:
            blocks = [
                grid[Cy][Cx],
                grid[Cy + 1][Cx],
                grid[Cy + 1][Cx - 1],
                grid[Cy][Cx + 1],
            ]
        if R == 90 or R == 270:
            blocks = [
                grid[Cy][Cx],
                grid[Cy][Cx - 1],
                grid[Cy - 1][Cx - 1],
                grid[Cy + 1][Cx],
            ]

    if TetType == "TETROMINO_Z":
        if R == 0 or R == 180:
            blocks = [
                grid[Cy][Cx],
                grid[Cy + 1][Cx],
                grid[Cy + 1][Cx + 1],
                grid[Cy][Cx - 1],
            ]
        if R == 90 or R == 270:
            blocks = [
                grid[Cy][Cx],
                grid[Cy - 1][Cx],
                grid[Cy + 1][Cx - 1],
                grid[Cy][Cx - 1],
            ]

    return blocks


def rotationCollider(TetType, Cx, Cy, R, grid):

    try:

        blocks = getBlocks(TetType, Cx, Cy, R + 90, grid)
        for i in blocks:

            if i[0] == "P":

                return True

    except IndexError:

        pass
    return False


def BoxCollider(TetType, Cx, Cy, R, grid):
    collision = False
    try:
        blocks = getBlocks(TetType, Cx, Cy + 1, R, grid)
        for i in blocks:
            if i[0] == "P":
                collision = True
                break

    except IndexError:
        collision = True
        pass
    return collision


def BoxColliderOLD(TetType, Cx, Cy, R, grid):
    collision = False

    try:
        if TetType == "SINGLE_BLOCK":
            if grid[Cy + 1][Cx][0] == "P":
                collision = True
            if Cy + 1 == 20:
                collision = True
        if TetType == "TETROMINO_I":
            if R == 0:
                if (
                    (grid[Cy + 1][Cx][0] == "P")
                    or (grid[Cy + 1][Cx + 1][0] == "P")
                    or (grid[Cy + 1][Cx - 1][0] == "P")
                    or (grid[Cy + 1][Cx + 2][0] == "P")
                ):
                    collision = True
                if Cy + 1 == 20:
                    collision = True
            elif R == 90:
                if Cy == 17:
                    collision = True
                if grid[Cy + 3][Cx][0] == "P":
                    collision = True
            elif R == 180:
                if (
                    (grid[Cy + 1][Cx][0] == "P")
                    or (grid[Cy + 1][Cx + 1][0] == "P")
                    or (grid[Cy + 1][Cx - 2][0] == "P")
                    or (grid[Cy + 1][Cx - 1][0] == "P")
                ):
                    collision = True
                if Cy + 1 == 20:
                    collision = True
            elif R == 270:
                if Cy + 2 == 20:
                    collision = True
                if grid[Cy + 2][Cx][0] == "P":
                    collision = True

        if TetType == "TETROMINO_O":
            if Cy + 2 == 20:
                collision = True
            if (grid[Cy + 2][Cx][0] == "P") or (grid[Cy + 2][Cx + 1][0] == "P"):
                collision = True
        if TetType == "TETROMINO_T":
            if Cy + 2 == 20:
                collision = True
            if (
                (grid[Cy + 2][Cx][0] == "P")
                or (grid[Cy + 1][Cx + 1][0] == "P")
                or (grid[Cy + 1][Cx - 1][0] == "P")
            ):
                collision = True
        if TetType == "TETROMINO_J":
            if Cy + 3 == 20:
                collision = True
            if (grid[Cy + 3][Cx][0] == "P") or (grid[Cy + 3][Cx - 1][0] == "P"):
                collision = True
        if TetType == "TETROMINO_L":
            if Cy + 3 == 20:
                collision = True
            if (grid[Cy + 3][Cx][0] == "P") or (grid[Cy + 3][Cx + 1][0] == "P"):
                collision = True
        if TetType == "TETROMINO_S":
            if Cy + 2 == 20:
                collision = True
            if (
                (grid[Cy + 2][Cx][0] == "P")
                or (grid[Cy + 1][Cx + 1][0] == "P")
                or (grid[Cy + 2][Cx - 1][0] == "P")
            ):
                collision = True
        if TetType == "TETROMINO_Z":
            if Cy + 2 == 20:
                collision = True
            if (
                (grid[Cy + 2][Cx][0] == "P")
                or (grid[Cy + 2][Cx + 1][0] == "P")
                or (grid[Cy + 1][Cx - 1][0] == "P")
            ):
                collision = True

    except IndexError:
        pass

    return collision


"""
colliding = False
GRID_ = Grid(10,20)
for i in range(20):
    if colliding == False:
        displayMapRefresh(GRID_)
        colliding = BoxCollider("TETROMINO_I",1,i,0,GRID_)
        displayMap("TETROMINO_I",1,i,0,GRID_)  
        DisplayMapTest(GRID_)
        time.sleep(0.1)
        os.system('clear')
    
SolidifyTetrominos(GRID_) 
DisplayMapTest(GRID_)

colliding = False  
for i in range(20):
    if colliding == False:
        displayMapRefresh(GRID_)
        colliding = BoxCollider("TETROMINO_O",1,i,0,GRID_)
        displayMap("TETROMINO_O",1,i,0,GRID_)  
        DisplayMapTest(GRID_)
        time.sleep(0.1)
        os.system('clear')
    
SolidifyTetrominos(GRID_)   
"""


def displayReLink(grid, Dgrid):
    # print(TetType)
    Cs = []

    for i in range(len(grid)):

        for j in range(len(grid[0])):

            if grid[i][j][0] == "P":
                TetType = grid[i][j][1]
                if TetType == "s":
                    Tet = [
                        " \x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588 ",
                        " \x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588 ",
                    ]
                if TetType == "i":
                    Tet = [
                        " \x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588 ",
                        " \x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588 ",
                    ]

                if TetType == "o":
                    Tet = [
                        " \x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588 ",
                        " \x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588 ",
                    ]
                if TetType == "t":
                    Tet = [
                        " \x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588 ",
                        " \x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588 ",
                    ]
                if TetType == "j":
                    Tet = [
                        " \x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588 ",
                        " \x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588 ",
                    ]
                if TetType == "l":
                    Tet = [
                        " \x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588 ",
                        " \x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588 ",
                    ]
                if TetType == "s":
                    Tet = [
                        " \x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588 ",
                        " \x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588 ",
                    ]
                if TetType == "z":
                    Tet = [
                        " \x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588 ",
                        " \x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588 ",
                    ]
                Dgrid[(3 * i) + 3][j + 1] = Tet[0]
                Dgrid[(3 * i) + 4][j + 1] = Tet[1]
                # Cs.append([i,j,True])


def displayLink(grid, Dgrid, TetType):
    # print(TetType)
    Cs = []
    if TetType == "SINGLE_BLOCK":
        Tet = [
            " \x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588 ",
            " \x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588\x1b[38;2;15;82;186m\u2588 ",
        ]
    if TetType == "TETROMINO_I":
        Tet = [
            " \x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588 ",
            " \x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588\x1b[38;2;90;201;202m\u2588 ",
        ]

    if TetType == "TETROMINO_O":
        Tet = [
            " \x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588 ",
            " \x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588\x1b[38;2;204;202;65m\u2588 ",
        ]
    if TetType == "TETROMINO_T":
        Tet = [
            " \x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588 ",
            " \x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588\x1b[38;2;139;41;196m\u2588 ",
        ]
    if TetType == "TETROMINO_J":
        Tet = [
            " \x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588 ",
            " \x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588\x1b[38;2;0;28;195m\u2588 ",
        ]
    if TetType == "TETROMINO_L":
        Tet = [
            " \x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588 ",
            " \x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588\x1b[38;2;191;106;39m\u2588 ",
        ]
    if TetType == "TETROMINO_S":
        Tet = [
            " \x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588 ",
            " \x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588\x1b[38;2;92;199;59m\u2588 ",
        ]
    if TetType == "TETROMINO_Z":
        Tet = [
            " \x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588 ",
            " \x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588\x1b[38;2;188;38;26m\u2588 ",
        ]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j][0] == "B":

                Dgrid[(3 * i) + 3][j + 1] = Tet[0]
                Dgrid[(3 * i) + 4][j + 1] = Tet[1]

            # Cs.append([i,j,True])
            # if grid[i][j][0]  == 'P':
            # Cs.append([i,j,'null'])
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            Dgrid[i][j] = Tet[0]
            Dgrid[i+1][j] = Tet[1]"""

    # print(' ')
    # print(GRID_[i+1][1] ) , (GRID_[i+1][1+1] ) , (GRID_[i+1][1-1] ) , (GRID_[i+1][1+2] )


# DisplayMapTest(GRID_)


def Debug():
    GRID_ = Grid(10, 20)
    # DISPLAY_GRID_FRONT =genGrid(12,65)
    # DISPLAY_GRID_BACK =genGrid(12,65)
    # displayGrid((DISPLAY_GRID_FRONT))
    # time.sleep(0.1)
    # os.system('clear')
    colliding = False
    global NotOver
    global INP

    while NotOver:
        # Tetronminos = ["TETROMINO_O","TETROMINO_I","TETROMINO_T","TETROMINO_J","TETROMINO_L","TETROMINO_S","TETROMINO_Z"]
        Tetronminos = [
            "TETROMINO_O",
            "TETROMINO_I",
            "TETROMINO_T",
            "TETROMINO_J",
            "TETROMINO_L",
            "TETROMINO_S",
            "TETROMINO_Z",
        ]
        TetType_ = random.choice(Tetronminos)
        Cx = Spawn(TetType_)

        for i in range(20):

            if colliding == False:
                boundryCollision = BoundryCollider(
                    TetType_,
                    Cx,
                    i,
                    0,
                )
                sideCollisionR = sideblockCollider(GRID_, TetType_, Cx, i, 0, "R")
                sideCollisionL = sideblockCollider(GRID_, TetType_, Cx, i, 0, "L")
                Cx = ProccessInputs(
                    TetType_,
                    INP[2],
                    Cx,
                    boundryCollision,
                    sideCollisionR,
                    sideCollisionL,
                )

                INP = [0, 0, 0]
                displayMapRefresh(GRID_)
                colliding = BoxCollider(TetType_, Cx, i, 0, GRID_)

                displayMap(TetType_, Cx, i, 0, GRID_)
                # displayLink(GRID_,DISPLAY_GRID_BACK,TetType_)

                DisplayMapTest(GRID_)
                # displayGrid(DISPLAY_GRID_BACK)
                # if (i!= 19) and (colliding == False):
                # DISPLAY_GRID_BACK = linkRenders(DISPLAY_GRID_FRONT,DISPLAY_GRID_BACK )

                time.sleep(0.1)
                os.system("clear")
        SolidifyTetrominos(GRID_)
        DisplayMapTest(GRID_)
        # displayLink(GRID_,DISPLAY_GRID_BACK,TetType_)
        # displayGrid((DISPLAY_GRID_BACK))
        time.sleep(0.1)
        os.system("clear")
        # DISPLAY_GRID_FRONT = linkRenders(DISPLAY_GRID_BACK,DISPLAY_GRID_FRONT )
        colliding = False
        NotOver = not GameOver(GRID_)


def sound():
    global NOTend
    audio_file = "/Users/sohanprabhu/Desktop/TETRIS/Original Tetris theme (Tetris Soundtrack).mp3"
    x = 0
    while NOTend:

        subprocess.call(["afplay", audio_file])


QUIT = False


def menu():
    global MENU
    iNP = [27, 91, 65]

    global QUIT
    while MENU:
        # print(iNP)
        if iNP[2] == 66:
            x = 0
            Screen(
                "/Users/sohanprabhu/Desktop/TETRIS/Tetris_2.jpeg"
            )  # fix image quailties

        if iNP[2] == 65:
            x = 1
            Screen("/Users/sohanprabhu/Desktop/TETRIS/Tetris_1.jpeg")
        if iNP[2] == 10:
            if x == 0:
                MENU = False

                QUIT = True

            if x == 1:
                MENU = False

        if iNP[2] != 10:
            keyTypes = [65, 66, 91, 27]
            for i in range(3):
                if iNP[2] != 10:
                    key = ord(sys.stdin.read(1))
                    # print(key)
                if key == 10:
                    iNP = [0, 0, 10]

                if key in keyTypes:
                    if key not in iNP:
                        iNP[i] = key

        time.sleep(0.1)
        os.system("clear")


NOTend = True


def main():
    tty.setcbreak(sys.stdin)
    global MENU
    global NotOver
    global QUIT
    global NOTend

    """
    if not t3.is_alive():
                        t3 = None
                        t3 = threading.Thread(target = sound)
                        t3.start()
    """
    t4 = threading.Thread(target=menu)
    t3 = threading.Thread(target=sound)
    t2 = threading.Thread(target=usrInp)
    t1 = threading.Thread(target=displayGame)
    t3.start()

    t4.start()
    t4.join()
    if QUIT == True:
        NOTend = False
        os.system("killall afplay")
        sys.exit()

    while NOTend:
        # print(NOTend)
        if MENU == False:
            if (not t1.is_alive()) and (not t2.is_alive()):
                os.system("reset")
                t2 = None
                t1 = None
                sys.stdin = os.fdopen(0)
                tty.setcbreak(sys.stdin)

                t2 = threading.Thread(target=usrInp)
                t1 = threading.Thread(target=displayGame)
                t1.start()
                t2.start()
                t1.join()
                if NotOver == False:
                    NOTend = False
                    os.system("killall afplay")
                    sys.exit()

        if MENU == True:
            # print(QUIT)
            if not t4.is_alive():
                # print(MENU)
                t4 = None

                t4 = threading.Thread(target=menu)
                t4.start()
                t4.join()
                if QUIT == True:
                    NOTend = False
                    os.system("killall afplay")
                    sys.exit()


main()
os.system("killall afplay")
sys.exit()


# print(' \x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588 \x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588'*6)
# print(' \x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588 \x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588\x1b[38;2;255;255;255m\u2588'*6)
