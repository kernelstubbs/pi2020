import unicornhat as hat
from time import sleep

hat.set_layout(hat.AUTO)
hat.rotation(90)
hat.brightness(0.3)

def display(duration): # Instead of repeating these three lines throughout, we can call them as display()
        hat.show()
        sleep(duration)
        hat.clear()


colours = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255), 
    'fucshia': (255, 0, 170)
    }

# Take input from the user and convert it to lowercase
selection = (input("Input colour (red, green, blue, fucshia): ")).lower()

if selection in colours:
    colour = colours[selection]
    hat.set_all(colour)
    display(3)
else:
    print("I don't know that colour.")