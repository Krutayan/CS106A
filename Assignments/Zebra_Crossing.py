"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        paint_column()
        if front_is_clear():
            pass_3unit()

def paint_column():
    # pre : facing east at bottom row
    #post : facing east at bottom row displaced by 1 X Co-ord units
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()  # fench post problem
    change_column()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper() # fench post promblem
    turn_left()

def pass_3unit():
    # karel displaced by 4 X Co-Ord units
    if front_is_clear():
        for i in range (4):
            move()

def change_column():
    turn_right()
    move()
    turn_right()

def turn_right():
    for i in range (3):
        turn_left()






# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
