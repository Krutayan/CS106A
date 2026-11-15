"""
Assignment: Archway (Worked Example)
Course: Stanford CS106A
Filename: archway.py

Description:
A Karel the Robot example demonstrating how Karel navigates up, over, 
and down an archway structure using conditional movement helper functions 
like `move_to_wall` and custom turns[cite: 16].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work![cite: 16]
"""

from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.[cite: 16]
    """
    turn_left()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_right()
    move_to_wall()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()
        

# There is no need to edit code beyond this point[cite: 16]

if __name__ == '__main__':
    main()
