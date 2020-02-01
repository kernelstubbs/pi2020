#!/usr/bin/env python

import sys, termios, tty, os, time, re
import unicornhat as hat

hat.set_layout(hat.AUTO)
hat.rotation(90)
hat.brightness(0.25)
width,height=hat.get_shape()

print(width)
print(height)
button_delay = 0.2

f = open('8x8ascii', 'r+')
ascii = [line for line in f.readlines()]
f.close()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def show_key(grid):
    asciipic = []
    for octet in grid.split(","):
        asciipic.append(octet)

    for h in range(height):
        for w in range(width):
            io = asciipic[h][w]
            if io == '1':
                hat.set_pixel(w, h, 255, 0, 0)
            else:
                hat.set_pixel(w, h, 0, 0, 0)
    hat.show()

while True:
    char = getch()
    if ord(char) == 27: # ESC
        quit()
    elif ord(char) > len(ascii):
        continue
    else:
        value = ascii[ord(char)-1]
        if value == '\n':  # skip blank lines
            continue
        else:
            grid = (re.search(r"\[(\S+)\]", value)).group(1)
            show_key(grid)