"""
Assignment: Move Beeper (Worked Example)
Course: Stanford CS106A
Filename: move_beeper.py

Description:
A Karel the Robot example demonstrating how Karel picks up a beeper 
from its initial position, navigates through the world, and places 
it down at the correct target location using custom right-turn helper 
functions[cite: 14].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work![cite: 14]
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.[cite: 14]
    """
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_left()
    move()
    move()
    turn_right()
    move()
    turn_right()
    move()
    put_beeper()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point[cite: 14]

if __name__ == '__main__':
    main()
