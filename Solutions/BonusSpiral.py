import unicornhat as hat
from time import sleep

hat.rotation(90)
hat.brightness(0.25)        
width,height = hat.get_shape() # Universal for hat and hatHD 8x8 or 16x16 grids


red     = (255, 0, 0)

def display(duration):
        hat.show()
        sleep(duration)

xLower = 0
xUpper = width - 1
yLower = 0
yUpper = height - 1


while xUpper > xLower:
    for y in range(yLower,yUpper + 1):
        hat.set_pixel(xLower, y, *red)
        display(0.2)
    xLower += 1
    for x in range(xLower,xUpper + 1):
        hat.set_pixel(x, yUpper, *red)
        display(0.2)
    yUpper -= 1
    for y in range(yUpper, yLower - 1, -1):
        hat.set_pixel(xUpper, y, *red)
        display(0.2)
    xUpper -= 1
    for x in range(xUpper, xLower - 1, -1):
        hat.set_pixel(x, yLower, *red)
        display(0.2)
    yLower += 1