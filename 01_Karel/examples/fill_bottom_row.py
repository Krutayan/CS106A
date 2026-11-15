"""
Assignment: Fill Bottom Row (Worked Example)
Course: Stanford CS106A
Filename: fill_bottom_row.py

Description:
A Karel the Robot example demonstrating how to solve the classic 
fencepost problem using an initial beeper placement followed by a 
while-loop to fill the entire bottom row of any-sized world[cite: 15].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work![cite: 15]
"""

from karel.stanfordkarel import *

def main():
    """
    Fills entire bottom row of any sized world with beepers.[cite: 15]
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
        

# There is no need to edit code beyond this point[cite: 15]

if __name__ == '__main__':
    main()
