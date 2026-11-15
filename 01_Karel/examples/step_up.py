"""
Assignment: Step Up (Worked Example)
Course: Stanford CS106A
Filename: step_up.py

Description:
A foundational Karel the Robot example demonstrating how Karel 
navigates upward over a ledge, picks up a beeper, climbs onto the 
platform, and places the beeper down using a custom helper function 
for right turns[cite: 13].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work![cite: 13]
"""

# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
