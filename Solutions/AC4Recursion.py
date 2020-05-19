import unicornhat as hat
from time import sleep

hat.set_layout(hat.AUTO)
hat.rotation(90)
hat.brightness(0.4)        
width,height = hat.get_shape() # Universal for hat and hatHD 8x8 or 16x16 grids

red     = (255, 0, 0)
green   = (0, 255, 0)
blue    = (0, 0, 255)
fucshia = (255, 0, 170)
off     = (0, 0, 0)

def display(duration): # Instead of repeating these three lines throughout, we can call them as display()
        hat.show()
        sleep(duration)
        hat.clear()


##
### Challenge #4
### Use recursion to create a reducing square rainbow
##

def recurse(step):
    p1 = width - step
    colour = ((1 / width * p1), 1, 1)
    for p2 in range(p1 + 1):
            hat.set_pixel_hsv(p1, p2, *colour)
            if p1 != p2:
                hat.set_pixel_hsv(p2, p1, *colour)
    hat.show()
    sleep(2)
    if step < width:
        recurse(step + 1)
recurse(1)



## Method ONE - decreasing squares - 204 set_pixel calls / 1496 for hatHD

for n in range(width):
    i = width - n
    colour = ((1 / width * i), 1, 1)
    for x in range(i):
        for y in range(i):
            hat.set_pixel_hsv(x, y, *colour)
display(5)

## Method TWO - focused recursion - 72 set_pixel calls / 272 for hatHD

for n in range(width):
    p1 = width - n
    colour = ((1 / width * p1), 1, 1)
    for p2 in range(p1 + 1):
            hat.set_pixel_hsv(p1, p2, *colour)
            hat.set_pixel_hsv(p2, p1, *colour)
display(5)

## Method THREE - focused and efficient recursion - 64 set_pixel calls / 256 for hatHD

for n in range(width):
    p1 = width - n
    colour = ((1 / width * p1), 1, 1)
    for p2 in range(p1 + 1):
            hat.set_pixel_hsv(p1, p2, *colour)
            if p1 != p2:
                hat.set_pixel_hsv(p2, p1, *colour)
display(5)


if False:
    '''
width = 8
count = 0
for i in range(width):
    n = width - i
    for x in range(n+1):
        for y in range(n+1):
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
'''