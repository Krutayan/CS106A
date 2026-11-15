"""
Assignment: Rainbow (Worked Example)
Course: Stanford CS106A
Filename: rainbow.py

Description:
A Karel the Robot example demonstrating corner-painting functionality 
where Karel paints sequential squares in red, orange, yellow, green, 
and blue across a 1-row world[cite: 17].
"""

"""
File: Rainbow.py
------------------------------
Karel makes a rainbow![cite: 17]
"""

"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!

Note: The unit test for this worked example is currently not working. Ignore it![cite: 17]
"""

from karel.stanfordkarel import *

def main():
    """
    Karel paints squares with the colors red, orange, yellow, green, and blue, 
    moving across the world and finishing in the rightmost spot.
    """
    paint_corner('red')
    move()
    paint_corner('orange')
    move()
    paint_corner('yellow')
    move()
    paint_corner('green')
    move()
    paint_corner('blue')
    move()
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
