"""
Assignment: Move 5 (Worked Example)
Course: Stanford CS106A
Filename: move_5.py

Description:
A Karel the Robot example demonstrating basic control flow 
and loops to make Karel move forward 5 times consecutively[cite: 19].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work![cite: 19]
"""

from karel.stanfordkarel import *

def main():
    """
    Moves forward 5 times[cite: 19]
    """
    for i in range (5):
        move()

# There is no need to edit code beyond this point[cite: 19]

if __name__ == '__main__':
    main()
