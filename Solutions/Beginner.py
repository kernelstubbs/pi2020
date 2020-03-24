import unicornhat as hat
import time

hat.set_layout(hat.AUTO)
hat.rotation(90)
hat.brightness(0.25)        
col,row = hat.get_shape() # Universal for hat and hatHD 8x8 or 16x16 grids

red     = (255, 0, 0)
green   = (0, 255, 0)
blue    = (0, 0, 255)

##
### Challenge/Tutorial #1
### Make a slash from 0-0 to 7-7 using 8 calls to set_pixel()
##

hat.set_pixel(0, 0, *red)
hat.set_pixel(1, 1, *red)
hat.set_pixel(2, 2, *red)
hat.set_pixel(3, 3, *red)
hat.set_pixel(4, 4, *red)
hat.set_pixel(5, 5, *red)
hat.set_pixel(6, 6, *red)
hat.set_pixel(7, 7, *red)

hat.show()
time.sleep(5)
hat.clear()

##
### Challenge #2
### Do the same, but using a FOR loop to use only one set_pixel() line
##

for i in range(col):
    x = i
    y = i
    hat.set_pixel(x,y, *blue)

hat.show()
time.sleep(5)
hat.clear()

##
### Challenge #3
### Switch the slash from the previous challenges to go from 0-7 to 7-0
##

for i in range(col):
    x = i
    y = 7 - i
    hat.set_pixel(x, y, *green)
hat.show()
time.sleep(5)
hat.clear()

##
### Challenge #4
### Light one column using a FOR loop
##

y = 0 # which column to light 0-7
for x in range(col):
    hat.set_pixel(x, y, *red)

hat.show()
time.sleep(5)
hat.clear()

##
### Challenge #5
### Light one row using a FOR loop
##

x = 0 # which column to light 0-7
for y in range(row):
    hat.set_pixel(x, y, *red)

hat.show()
time.sleep(5)
hat.clear()

##
### BONUS - Make an X
##

for i in range(col):
    x1 = i
    x2 = 7 - i
    y = i
    hat.set_pixel(x1, y, *red)
    hat.set_pixel(x2, y, *blue)
hat.show()
time.sleep(5)
hat.clear()