import sys ,tty

def usrInp(shipAxis,shipType):
    notRecived = True
    Input = [0,0,0]
    enterCheck = False
    delCheck = False
    end = False
    keyTypes = [65,66,67,68,91,27]
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
            if key == 118:
                shipAxis = 'verticle'
            if key == 104 :
                shipAxis = 'horizontal'
            if key == 119 :
                shipType = 'warship'
            if key == 115 :
                shipType = 'submarine'
            if key == 99 :
                end = True
            break
    return [ Input,enterCheck,delCheck,shipAxis,shipType,end]