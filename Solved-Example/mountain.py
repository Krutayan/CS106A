from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size
and plants a beeper at the top
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

def main():
    climb_mountain()
    plant_the_flag()
    decend_mountain()
    

def climb_mountain():
    #pre: karel is at (1,1) and facing east.
    #post: karel is at (5,5) and facing east.
    while front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()

def plant_the_flag():
    #put beeper at top
    put_beeper()

def decend_mountain():
    #pre: karel at (5,5) and facing east
    #post: karel at (9.1) and facing east
    while front_is_clear():
        move()
        turn_right()
        move()
        turn_left()

def turn_right():
    for i in range (3):
        turn_left()





if __name__ == '__main__':
    main()
