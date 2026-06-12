from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()
    turn_back()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_back()


    # add your code here
# command creating for right turn   
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# creating command for back turn    
def turn_back():
    turn_left()
    turn_left()    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
