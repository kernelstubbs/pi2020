xRange, yRange = 6,6

import sys, termios, tty 
import random
import os

class Snake:
    def __init__(self, x, y):
        self.pos = [[x,y]]
    def show(self):
        for y in reversed(range(yRange)):
            for x in range(xRange):
                coord = [x+1,y+1]
                if coord in self.pos:
                    if coord ==  self.pos[0]:
                        print("X", end='')
                    else:
                        print("O", end='')
                elif coord == food:
                    print("*", end='')
                else:
                    print("_", end='')
            print('')
    def move(self, axis):
        x = int(self.pos[0][0])
        y = int(self.pos[0][1])
        
        if axis == "up":
            pos = [x,y+1]
        elif axis == "down":
            pos = [x,y-1]
        elif axis == "left":
            pos = [x-1,y]
        elif axis == "right":
            pos = [x+1,y]
        else:
            print("Invalid")
            return
        if pos in self.pos:
            if pos == self.pos[1]:
                return
            else:
                print("Game Over")
                exit() # game over screen or skull
        if pos[0]-1 in range(xRange) and pos[1]-1 in range(yRange):
            self.pos.insert(0, pos)
            if self.pos[0] == food:
                getFood()
            else:
                self.pos.pop()
        else:
            return

def getch():    # ref: http://code.activestate.com/recipes/134892/
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(3)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def getAxis():
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
    return dir

def getFood():
    global food
    if len(snake.pos) >= (xRange * yRange):
        print("A WINNER IS YOU!!!!")
        exit()
    while food in snake.pos:
        x = random.randint(1,xRange)
        y = random.randint(1,yRange)
        food = [x,y]

snake = Snake(1,1)
food = [1,1]
getFood()
snake.show()


while True:
    os.system('clear')
    print("\nUse arrow keys.  ESC x3 to exit(LOL)\n")
    snake.show()
    dir = getAxis()
    snake.move(dir)