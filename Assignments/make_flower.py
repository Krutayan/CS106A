"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    move_to_wall()
    ascend_stem()
    make_flower()
    descend_stem()
    move_to_wall()
    ascend_stem()
    make_flower()
    descend_stem()
    move_to_wall()

def move_to_wall():
    while front_is_clear():
        move()

def ascend_stem():
    turn_left()
    while right_is_blocked():
        move()

def make_flower():
    for i in range (2):
        put_beeper()
        move()
        turn_right()
    put_beeper()
    move()
    put_beeper()

def descend_stem():
    move_to_wall()
    turn_left()

def turn_right():
    for i in range (3):
        turn_left()



# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
