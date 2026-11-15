"""
Assignment: Clean Up Karel (Worked Example)
Course: Stanford CS106A
Filename: clean_up_karel.py

Description:
A Karel the Robot example demonstrating code decomposition and modular design, 
refactoring a messy flat script into clean, readable helper functions to 
clean up all beepers across multiple rows.
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: This starter code is a solution, but it's messy! Try decomposing it. If you need help, try looking at some of the comments for ideas on what to decompose.
"""

from karel.stanfordkarel import *

def main():
    """
    Cleans up beepers across multiple rows until reaching the top.
    """
    while left_is_clear():
        clean_row()
        return_to_start_of_row()
        move_to_next_row()
    
    # Clean up the final top row
    clean_row()

def clean_row():
    """
    Picks up all beepers along the current row.
    """
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    
    # Fencepost check for the last column
    if beepers_present():
        pick_beeper()

def return_to_start_of_row():
    """
    Turns Karel around and moves back to the first column.
    """
    turn_around()
    move_to_wall()
    turn_around()

def move_to_next_row():
    """
    Moves Karel up one row and re-orients to face East.
    """
    turn_left()
    move()
    turn_right()

def turn_around():
    """
    Turns Karel 180 degrees.
    """
    for i in range(2):
        turn_left()

def turn_right():
    """
    Turns Karel to the right.
    """
    for i in range(3):
        turn_left()

def move_to_wall():
    """
    Moves Karel forward until blocked by a wall.
    """
    while front_is_clear():
        move()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
