import queue
import random
import threading
import time
import unicornhat as uh

from readchar import readkey, key

SNAKE_INCREASE_LENGTH_VALUE = 1
SNAKE_LOWER_DELAY_VALUE = 0.02

GRID_UPPER_LIMIT = 7
GRID_LOWER_LIMIT = 0


# Initialize the unicorn hat brightness to be 50%
# and clear out anything that might have already
# been on the array.
def initUnicornHat():
    uh.brightness(0.2)
    uh.clear()
    uh.show()
    

# read_keyboard_input
#
# inputQueue - Queue to write any key inputs to.
#
# Listener thread that will take keyboard input
# and send it to the main program. This is how
# we will control the snake.
def read_keyboard_input(inputQueue):
    while (True):
        k = readkey()
        inputQueue.put(k)


# randomize_snake_colour
#        
# Randomly pick from a few possible colours of
# snake.
#
# Returns:
#  (red, green, blue) - A valid RGB colour combination
def randomize_snake_colour():
    possible_colour_list = [
        (  0,   0, 255),
        (  0, 255,   0),
        (  0, 255, 255),
        (255,   0,   0),
        (255, 255,   0)
    ]
    return (possible_colour_list[random.randrange(5)])
    

# generate_power_pill
#
# snakeLocations - List of the locations the snake
#                  occupies. The power pill cannot
#                  be there.
#
# Pick a location for the power pill. It cannot be
# placed on top of the currently existing snake.
# Once a valid location is found, also display it
# on the grid.
#
# Returns:
#   (x, y) - A valid coordinate set where the power
#            pill can exist.
def generate_power_pill(snakeLocations):
    validLocation = False
    
    while (not validLocation):
        x = random.randrange(GRID_UPPER_LIMIT)
        y = random.randrange(GRID_UPPER_LIMIT)
    
        if (x, y) not in snakeLocations:
            validLocation = True
    
    print("Generated power pill at: (" + str(x) + "," + str(y) + ")")
    uh.set_pixel(x, y, 255, 0, 255)
    uh.show()
    
    return (x, y)


# snake_has_crashed
#
# x - Current x location of the snake.
# y - Current y location of the snake.
# locationList - List of locations the snake occupies
#
# Checks to see if the snake has run off the edge of
# the grid, or run into itself.
#
# Returns:
#  True - Snake has crashed
#  False - Snake has not crashed
def snake_has_crashed(x, y, locationList):
    # Snake has run off the edge of the display grid
    if ((x > GRID_UPPER_LIMIT) or
        (x < GRID_LOWER_LIMIT) or
        (y > GRID_UPPER_LIMIT) or
        (y < GRID_LOWER_LIMIT)):
        print("Ran off edge of grid")
        return True
    
    # Snake has hit itself
    if ((x, y) in locationList):
        print("Snake hit itself")
        return True
    
    # Snake is ok
    return False


# main()
#
# Run main snake loop.
def main():
    
    # Current (x, y) coordinates of the head of the snake
    snake_x = 0
    snake_y = 0
    
    # Snake length (also correlates to the score)
    snake_length = 1
    
    # How much delay to have in the loop (how fast is the
    # snake going?)
    snake_delay = 0.5
    
    # Array of all the bits of the snake. Head is at 0,
    # tail is at the end.
    snake_location_list = [(0, 0)]
    
    # What direction are we going in? +1, 0 or -1
    snake_x_dir = 1
    snake_y_dir = 0
    
    initUnicornHat()
    
    # Create and start thread to listen to the keyboard
    inputQueue = queue.Queue()
    inputThread = threading.Thread(target = read_keyboard_input, args = (inputQueue, ), daemon = True)
    inputThread.start()
    
    # Pick a random colour for the snake
    red, green, blue = randomize_snake_colour()
    
    # Randomly place the power pill, it cannot be where
    # the snake currently is
    power_x, power_y = generate_power_pill(snake_location_list)
    
    # Start the snake at (0, 0) to begin
    uh.set_pixel(snake_x, snake_y, red, green, blue)
    uh.show()
    time.sleep(snake_delay)
    
    while (True):
        # Check the queue to see if a kay has been pressed,
        # and if so, change the direction as needed.
        if (inputQueue.qsize() > 0):
            keyPressed = inputQueue.get()
            if (keyPressed == key.DOWN):
                snake_x_dir = 0
                snake_y_dir = -1
                
            if (keyPressed == key.UP):
                snake_x_dir = 0
                snake_y_dir = 1
                
            if (keyPressed == key.LEFT):
                snake_x_dir = 1
                snake_y_dir = 0
                
            if (keyPressed == key.RIGHT):
                snake_x_dir = -1
                snake_y_dir = 0
        
        # Update the snake with its new coordinates
        snake_x += snake_x_dir
        snake_y += snake_y_dir
        
        # If the snake has crashed, then display the game over message
        if (snake_has_crashed(snake_x, snake_y, snake_location_list)):
            uh.set_all(255, 0, 0)
            uh.show()
            print("Oops, game over!!")
            print("")
            print("Your score was: " + str(snake_length - 1))
            print("Press CTRL-C to quit...")
            inputThread.join()
            return
        
        # Add the new snake location to the list
        snake_location_list.insert(0, (snake_x, snake_y))
        
        # Remove the tail of the snake to take into account
        # snake movement
        if (len(snake_location_list) > snake_length):
            endX, endY = snake_location_list.pop()
            uh.set_pixel(endX, endY, 0, 0, 0)
        
        # If the snake hit a power pill, then:
        #   - Generate a new power pill
        #   - Add one to the length
        #   - Speed up the snake a little bit
        if ((snake_x == power_x) and (snake_y == power_y)):
            power_x, power_y = generate_power_pill(snake_location_list)
            snake_length += SNAKE_INCREASE_LENGTH_VALUE
            if (snake_delay > SNAKE_LOWER_DELAY_VALUE):
                snake_delay -= SNAKE_LOWER_DELAY_VALUE
        
        # Display the whole snake
        for (x, y) in snake_location_list:
            uh.set_pixel(x, y, red, green, blue)
        uh.show()
        
        time.sleep(snake_delay)
    

if (__name__ == '__main__'):
    main()
