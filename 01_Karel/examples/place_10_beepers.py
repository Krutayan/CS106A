"""
Assignment: Place 10 Beepers (Worked Example)
Course: Stanford CS106A
Filename: place_10_beepers.py

Description:
A Karel the Robot example demonstrating how Karel uses a for loop 
to place 10 beepers on a single corner square[cite: 18].
"""

"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work![cite: 18]
"""

from karel.stanfordkarel import *

def main():
    """
    Places 10 beepers in the spot that Karel is standing.[cite: 18]
    """
    for i in range(10):
        put_beeper() # Delete this line and write your code here! :)[cite: 18]


# There is no need to edit code beyond this point[cite: 18]

if __name__ == '__main__':
    main()
