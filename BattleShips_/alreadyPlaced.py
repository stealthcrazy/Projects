'''
this program is checking whether player or computer is attacking an already attacked cordinate
'''

def AlreadyPlaced(x,y,board,type):
    alreadyPlaced = False 
    chars = ['A','B','C','D','E','F','G','H']
    x = chars.index(x.upper()) #converts letter to number from list
    attackColor = ['\x1b[38;2;255;0;0m\u2588','\x1b[38;2;255;255;0m\u2588'] # attack colors
    if board[y][x] in attackColor: # checks if the cordinate is already attacked
        alreadyPlaced = True
        if type ==1:
            print('                                            place some where else') # asks user to place somewhere else if cordinate is already attacked
    return alreadyPlaced # returns if True or False depending on whether the cordinate is attacked