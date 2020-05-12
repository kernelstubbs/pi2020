import unicornhat as hat
from time import sleep

hat.rotation(90)
hat.brightness(0.4)        
width,height = hat.get_shape() # Universal for hat and hatHD 8x8 or 16x16 grids


red     = (255, 0, 0)

def display(duration):
        hat.show()
        sleep(duration)

pixel = 1
xLower = 0
xUpper = width - 1
yLower = 0
yUpper = height - 1


while xUpper > xLower:
    for y in range(yLower,yUpper + 1):
        hat.set_pixel_hsv(xLower, y, (1 / (width * height) * pixel), 1, 1)
        display(0.2)
        pixel += 1
    xLower += 1
    for x in range(xLower,xUpper + 1):
        hat.set_pixel_hsv(x, yUpper,  (1 / (width * height) * pixel), 1, 1)
        display(0.2)
        pixel += 1
    yUpper -= 1
    for y in range(yUpper, yLower - 1, -1):
        hat.set_pixel_hsv(xUpper, y,  (1 / (width * height) * pixel), 1, 1)
        display(0.2)
        pixel += 1
    xUpper -= 1
    for x in range(xUpper, xLower - 1, -1):
        hat.set_pixel_hsv(x, yLower,  (1 / (width * height) * pixel), 1, 1)
        display(0.2)
        pixel += 1
    yLower += 1

sleep(5)

# SO what's going on here?
# We have four loops within a loop.  Each time, the 'range' is reduced in any given direction
# so that the fill starts in a narrower scope.

# Can it be reversed?  Try it!!

# Notes:
# 'range()' has three inputs:
#   1. The start of the range
#   2. The end of the range (remember we start at '0' which functionally excludes the last digit)
#   3. The 'increment' of the range...which for our purposes is negative

# += and -=
# These are the same as y = y + 1 or y = y - 1 (some other languages have a y++ or y-- function)

# display()
# We've made a custom function - you should do this whenever you have repeating snippets of code.




# BONUS!!!
# 1. Make the colour change each time the direction does
# 2. Change the colour of each dot slowly toward the center (hint: HUE / width * height)