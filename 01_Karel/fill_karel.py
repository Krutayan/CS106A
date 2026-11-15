"""
Assignment: Fill Karel (Assignment 1)
Course: Stanford CS106A
Filename: fill_karel.py

Description:
A Karel the Robot assignment demonstrating advanced loop structures 
and fencepost problem solving to fill an entire world of arbitrary size 
with beepers[cite: 15].
"""

from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.[cite: 15]
"""


def main():
    while left_is_clear():
        fill_row()
        come_back()
        change_row()
    fill_row()    #fench post problem

def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def come_back():
    turn_around()
    move_to_wall()
    turn_around()

def change_row():
    turn_left()
    move()
    turn_right()

def turn_around():
    for i in range (2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range (3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
