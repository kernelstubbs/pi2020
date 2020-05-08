#!/usr/bin/env python

import sys, termios, tty    # for getch - single character input
import re                   # regex parser
import unicornhat as hat

hat.set_layout(hat.AUTO)
hat.rotation(90)            # rotate based on the orientation of the hat 90-180-270
hat.brightness(0.25)        # setting this too high can result in discomfort
col,row = hat.get_shape()   # set the grid size

button_delay = 0.2          # allows hat the time the LEDs need to light

red     = [255,0,0]         # define some colours
green   = [0,255,0]
blue    = [0,0,255]
off     = [0,0,0]

f = open('8x8ascii', 'r+')  # opens 8x8ascii and breaks it into a numbered list
ascii = [line for line in f.readlines()]
f.close()

def getch():    # ref: http://code.activestate.com/recipes/134892/
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def show_key(grid,rgb):
    asciipic = []                               # list to hold the io grid
    for octet in grid.split(","):               # split the segments into lines
        asciipic.append(octet)                  # append each line to the list

    for y in range(row):                        # iterate through each row
        for x in range(col):                    # iterate through each column
            io = asciipic[y][x]                 # get the io value from our grid
            if io == '1':                       # if the value is '1' light the corresponding pixel
                hat.set_pixel(x, y, *rgb)       # X, Y, R, G, B
            else:                               # if it's anything other than '1' turn the corresponding pixel off
                hat.set_pixel(x, y, *off)       # X, Y, R, G, B
    hat.show()                                  # once the grid has been processed, light the hat

while True:
    char = getch()
    if ord(char) == 27:                 # ESC '^[' - includes arrows, ctl+, etc
        quit()
    elif ord(char) > len(ascii):        # skip if beyond scope of 8x8ascii
        continue
    else:
        value = ascii[ord(char)-1]      # because every good thing begins at zero
        if value == '\n':               # skip blank lines
            continue
        else:
            grid = (re.search(r"\[(\S+)\]", value)).group(1) # grab the bit between the [ ]
            
            if ord(char) in range(48,58):       # digits in blue
                rgb = blue
            elif ord(char) in range(65,91):     # lowercase letters in green
                rgb = green
            elif ord(char) in range (97,123):   # uppercase letters in green
                rgb = green
            else:
                rgb = red                       # everything else in red
            show_key(grid,rgb)                  # show me what you've got!