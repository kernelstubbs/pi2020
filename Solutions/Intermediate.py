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
### Challenge #1
### Make an oscillating dot, like Knight Rider or a Cylon
##

# Cylon

[int]y = row / 2 # place dot in teh middle-ish
for n in range(5):
    for i in range(col):
        x = i 
        hat.set_pixel(x, y, *red)
        hat.show()
        time.sleep(0.2)
        hat.clear()
    for i in range(col):
        x = 7 - i
        hat.set_pixel(x, y, *red)
        hat.show()
        time.sleep(0.2)
        hat.clear()