from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    while no_beepers_present():
        make_column()
        if front_is_clear():
            move_4units()

def make_column():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper() # fench post problem
    turn_around()
    move_to_wall()
    turn_left()

def move_4units():
    for i in range (4):
        move()

def turn_around():
    for i in range (2):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()



if __name__ == '__main__':
    main()
