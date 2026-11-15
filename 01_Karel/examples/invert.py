"""
Assignment: Invert (Worked Example)
Course: Stanford CS106A
Filename: invert.py

Description:
A Karel the Robot example demonstrating conditional control flow 
and while loops to invert a pattern of beepers across a single-row world[cite: 22].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Inverts the pattern of beepers in a single row world[cite: 22].
    """
    put_beeper()
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
        else:
            put_beeper()
         
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
