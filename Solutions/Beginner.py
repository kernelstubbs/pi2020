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
### Challenge - Light up a column of LEDs
##
y = 0 # which column to light 0-7
for x in range(col):
    hat.set_pixel(x,y, *red)

hat.show()
time.sleep(5)
hat.clear()

##
### Challenge - Make a /
##

for i in range(col):
    x = i
    y = i
    hat.set_pixel(x,y, *blue)

hat.show()
time.sleep(5)
hat.clear()

### Bonus - Make a \

for i in range(col):
    x = 7 - i
    y = i
    hat.set_pixel(x, y, *green)
hat.show()
time.sleep(5)
hat.clear()

##
### Challenge - Make an X
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