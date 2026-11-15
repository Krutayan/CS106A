"""
Assignment: Backflip (Worked Example)
Course: Stanford CS106A
Filename: backflip.py

Description:
A fun Karel the Robot example demonstrating how Karel uses a for loop 
to turn left 4 consecutive times to complete a full 360-degree spin[cite: 20].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work![cite: 20]
"""

from karel.stanfordkarel import *

def main():
    """
    Makes Karel do a sick backflip!![cite: 20]
    """
    for i in range (4):
        turn_left()
        


# There is no need to edit code beyond this point[cite: 20]

if __name__ == '__main__':
    main()
