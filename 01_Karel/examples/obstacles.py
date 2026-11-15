"""
Assignment: Obstacles (Worked Example)
Course: Stanford CS106A
Filename: obstacles.py

Description:
A Karel the Robot example demonstrating how Karel navigates over 
and around vertical wall obstacles in the bottom row, placing beepers 
immediately to the right of each obstacle using custom turn helper 
functions[cite: 15].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work![cite: 15]
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.[cite: 15]
    """
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_back()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_back()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    turn_left()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_back():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point[cite: 15]

if __name__ == '__main__':
    main()
