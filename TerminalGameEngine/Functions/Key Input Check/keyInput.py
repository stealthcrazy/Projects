import sys, tty

tty.setcbreak(sys.stdin)

key = ord(sys.stdin.read(4))
print(key)
'''
import sys, tty

tty.setcbreak(sys.stdin)
while True:
    key = sys.stdin.read(4)
    keysPressed = [ ord(i) for i in key ]
    print(keysPressed)'''