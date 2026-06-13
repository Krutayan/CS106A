# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

def main():
    # code for karel to what to do
    while left_is_clear():
        clear_floor()
        come_back()
        go_to_next_row()
    #fenchpost problem solution
    clear_floor()
    

def clear_floor():
    #it will pick beepers if present
    #pre: karel at first column facing east
    #post: karel at last column facing east
    while front_is_clear():  # at last column front is blocked
        if beepers_present():
            pick_beeper()
            move()
        else:
            move()  # if beepers not present than just move.
    if beepers_present():
        pick_beeper() #for beepers present in last column becaouse at last column front is blocked thus it does not execute the code"


def come_back():
    #after cleaning the beepers telling karel to come back at pre
    #pre: karel at last column facing east 
    #post: karel at first column facing east
    turn_around()
    move_to_wall()
    turn_around()

def go_to_next_row():
    #when one row is clear move to next one
    #after this karel is just one Y coordite dispaced is positive direction
    turn_left()
    move()
    turn_right()

def turn_around():
    for i in range (2):
        turn_left()
        #defining the turn around using left command

def turn_right():
    for i in range (3):
        turn_left()
        #defining right function using left function

def move_to_wall():
    while front_is_clear():
        move()



    


# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
