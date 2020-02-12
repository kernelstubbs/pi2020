import sys, termios, tty 

def getch():    # ref: http://code.activestate.com/recipes/134892/
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
dir = "null"   
while True:
    char = getch()
    if char == '\x1b[A':
        dir = "up"
    elif char == '\x1b[B':
        dir = "down"
    elif char == '\x1b[C':
        dir = "right"
    elif char == '\x1b[D':
        dir = "left"
    else:
        exit()
    print(dir)