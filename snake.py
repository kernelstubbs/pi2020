#import unicornhat as hat
#xRange, yRange = hat.getShape()
xRange, yRange = 8,8

import random

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
                print("invalid")
            else:
                print("Game Over")
                exit() # game over screen or skull
        self.pos.insert(0, pos)
        if self.pos[0] == food:
            getFood()
        else:
            self.pos.pop()

def getFood():
    global food
    while food in snake.pos:
        x = random.randint(1,xRange)
        y = random.randint(1,yRange)
        food = [x,y]

snake = Snake(1,1)
food = [1,1]
getFood()
snake.show()


while True:
    dir = input("Which way? up,down,left,right: ")
    snake.move(dir)
    snake.show()


