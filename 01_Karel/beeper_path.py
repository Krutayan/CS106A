"""
Assignment: Beeper Path
Course: Stanford CS106A
Filename: beeper_path.py

Description:
A Karel the Robot program where Karel follows a linear trail of 
beepers to navigate home dynamically using a while loop[cite: 12].
"""

from karel.stanfordkarel import *

def main():
    # we need to move karel by following beepers[cite: 12]
    while beepers_present():
        move()

# There is no need to edit code beyond this point[cite: 12]
if __name__ == '__main__':
    main()
