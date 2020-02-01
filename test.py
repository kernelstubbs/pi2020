#!/usr/bin/env python

import sys, termios, tty, os, time, re
 
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

def show_grid(grid):
    grid = grid.split(",")
    for line in grid:
        print(line)
    print("\n")

while True:
    char = getch()
    if ord(char) == 27: # ESC
        quit()
    elif ord(char) > len(ascii):
        continue
    else:
        value = ascii[ord(char)-1]
        if value == '\n':
            continue
        else:
            grid = (re.search(r"\[(\S+)\]", value)).group(1)
            show_grid(grid)