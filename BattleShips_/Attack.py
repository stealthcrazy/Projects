'''
program allows player to attack the computer board and display whether it is a hit or a miss on the attack display
'''

def attack(y,alpha,compBoard,attackBoard,playerHits,):
    chars = ['A','B','C','D','E','F','G','H']
    x = chars.index(alpha.upper()) # converts letter to number for X cordinate
    mainColor = ['\x1b[38;2;15;82;186m\u2588','\x1b[38;2;75;104;185m\u2588','\x1b[38;2;0;181;226m\u2588','\x1b[38;2;0;138;216m\u2588']  # ship colors
    if compBoard[y][x] in mainColor: # checks if the attack is a hit or a miss
        attackBoard[y][x] = '\x1b[38;2;255;0;0m\u2588'
        playerHits+=1
    else:
        attackBoard[y][x] = '\x1b[38;2;255;255;0m\u2588'
    return playerHits