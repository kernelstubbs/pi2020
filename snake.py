import unicornhat as hat
xRange, yRange = hat.get_shape()
#xRange, yRange = 8,8
hat.set_layout(hat.AUTO)           # rotate based on the orientation of the hat 90-180-270
hat.brightness(0.25) 

import sys, termios, tty 
import random
import time

red     = [255,0,0]         # define some colours
green   = [0,255,0]
blue    = [0,0,255]
off     = [0,0,0]

class Snake:
    def __init__(self, x, y):
        self.pos = [[x,y]]
    def show(self):
        for y in reversed(range(yRange)):
            for x in range(xRange):
                coord = [x+1,y+1]
                if coord in self.pos:
                    if coord ==  self.pos[0]:
                        hat.set_pixel(x, y, *blue)
                    else:
                        hat.set_pixel(x, y, *red)
                elif coord == food:
                    hat.set_pixel(x, y, *green)
                else:
                    hat.set_pixel(x, y, *off)
            hat.show()
    def move(self, axis):
        x = int(self.pos[0][0])
        y = int(self.pos[0][1])
        
        if axis == "up":
            pos = [x,y+1]
        elif axis == "down":
            pos = [x,y-1]
        elif axis == "left":
            pos = [x+1,y]
        elif axis == "right":
            pos = [x-1,y]
        else:
            end(*red)
        if pos in self.pos:
            if pos == self.pos[1]:
                end(*red)
            else:
                end(*red)
        if pos[0]-1 in range(xRange) and pos[1]-1 in range(yRange):
            self.pos.insert(0, pos)
            if self.pos[0] == food:
                getFood()
            else:
                self.pos.pop()
        else:
            end(*red)
    def __iter__(self):
        return self.pos.__iter__()

def end(*rgb):
    for i in range(3):
        hat.set_all(*rgb)
        hat.show()
        time.sleep(0.5)
        hat.clear()
        hat.show()
        time.sleep(0.5)
    exit()

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
        end(*green)
    while food in snake.pos:
        x = random.randint(1,xRange)
        y = random.randint(1,yRange)
        food = [x,y]

snake = Snake(1,1)
food = [1,1]
getFood()
snake.show()

print("Use arrow keys or Esc(x3) to exit(LOL)")
while True:
    dir = getAxis()
    snake.move(dir)
    snake.show()