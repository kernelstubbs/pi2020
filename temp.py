import keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        print("wow")
        
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        print("broke")
        break  # if user pressed a key other than the given key the loop will breakq