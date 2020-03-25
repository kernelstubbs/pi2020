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
        time.sleep(duration)
        hat.clear()


##
### Challenge #4
### Use recursion to create a reducing square rainbow
##

## Method ONE - decreasing squares - 204 set_pixel calls / 1496 for hatHD

for n in range(width):
    i = width - 1 - n
    colour = ((1 / width * n), 1, 1)
    for x in range(i):
        for y in range(i):
            set_pixel_hsv(x, y, *colour)

## Method TWO - focused recursion - 72 set_pixel calls / 272 for hatHD

for n in range(width):
    p1 = width - 1 - n
    colour = ((1 / width * n), 1, 1)
    for p2 in range(p1 + 1):
            set_pixel_hsv(p1, p2, *colour)
            set_pixel_hsv(p2, p1, *colour)

## Method THREE - focused and efficient recursion - 64 set_pixel calls / 256 for hatHD

for n in range(width):
    p1 = width - 1 - n
    colour = ((1 / width * n), 1, 1)
    for p2 in range(n):
            set_pixel_hsv(p1, p2, *colour)
            if p1 != p2:
                set_pixel_hsv(p2, p1, *colour)



width = 8
count = 0
for i in range(width):
    n = width - i
    for x in range(n):
        for y in range(n):
            print(x, y, end=' ')
            count += 1
        print()
    print('---')
print(count)

width = 8
count = 0
for n in range(width):
    p1 = width - 1 - n
    for p2 in range(p1 + 1):
        print(p1,p2, end=' ')
        print(p2, p1)
        count += 2
    print('---')
print(count)

width = 8
count = 0
for n in range(width):
    p1 = width - 1 - n
    for p2 in range(p1 + 1):
        print(p1, p2, end=' ')
        count += 1
        if p1 != p2:
            print(p2, p1, end=' ')
            count += 1
        print()
    print('---')
print(count)
