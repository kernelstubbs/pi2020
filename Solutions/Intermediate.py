import unicornhat as hat
from time import sleep

hat.set_layout(hat.AUTO)
hat.rotation(90)
hat.brightness(0.25)        
width,height = hat.get_shape() # Universal for hat and hatHD 8x8 or 16x16 grids

red     = (255, 0, 0)
green   = (0, 255, 0)
blue    = (0, 0, 255)
fucshia = (255, 0, 170)
off     = (0, 0, 0)

def display(duration): # Instead of repesting these three lines throughout, we can call them as display()
        hat.show()
        sleep(duration)
        hat.clear()

##
### Challenge #1
### Make an oscillating dot, like Knight Rider or a Cylon
##

y = int(height / 2) # place dot in the middle-ish
for n in range(5):
    for i in range(width):
        x = i 
        hat.set_pixel(x, y, *red)
        display(0.1)
    for i in range(width):
        x = width - 1 - i
        hat.set_pixel(x, y, *red)
        display(0.1)
# Why 'width - 1 - i' - Because width is equal to "8" but the pixel value can only be 0 to 7
# we offset to align with Pythonic ranges. 0-1-2-3 vs 1-2-3-4

## Bonus: Don't let the dot linger on the first or last position
## Hint: range(n,n)

y = int(height / 2) # place dot in the middle-ish
for n in range(5):
    for i in range(width):
        x = i 
        hat.set_pixel(x, y, *blue)
        display(0.1)
    for i in range(1,width - 1):
        x = width - 2 - i
        hat.set_pixel(x, y, *blue)
        display(0.1)

##
### Challenge #2
### Make an oscillating column in a non-primary colour
##

for n in range(5):
    for x in range(width):
        for y in range(height):
            hat.set_pixel(x, y, *fucshia)
        display(0.2)
    for i in range(1, width - 1):
        for y in range(height):
            x = width - 1 - i
            hat.set_pixel(x, y, *fucshia)
        display(0.2)

##
### Challenge #3
### Make a fire truck light
##

for n in range(10):
    for x in range(width):
        for y in range(height):
            hat.set_pixel(x, y, *red)
        hat.show()
        sleep(0.05)
    for x in range(width):
        for y in range(height):
            hat.set_pixel(x, y, *off)
        hat.show()
        sleep(0.05)

##
### Challenge #4
### Make a police light
##

for n in range(5):
    for x in range(width):
        for y in range(height):
            if x < width / 2:
                hat.set_pixel(x, y, *red)
            else:
                hat.set_pixel(x, y, *blue)
    display(0.2)
    for x in range(width):
        for y in range(height):
            if x < width / 2:
                hat.set_pixel(x, y, *blue)
            else:
                hat.set_pixel(x, y, *red)
    display(0.2)

##
### Challenge #5
### Light up only even columns (or rows) using only two FOR loops
### and using a range operator in the outer loop
##

for x in range(0, width, 2):
    for y in range(height):
        hat.set_pixel(x, y, *green)
display(5)
