from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    while left_is_clear():
        fill_row()
        come_back()
        change_row()
    fill_row()     #fench post problem

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
