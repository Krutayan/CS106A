"""
Assignment: Warmup
Course: Stanford CS106A
Filename: warmup.py

Description:
A foundational Karel the Robot program designed to practice basic control 
flow by moving forward, picking up a beeper, and continuing forward.
"""

from karel.stanfordkarel import *

# File: warmup.py
# -----------------------------
# The warmup program defines a "main"
# function which currently just has one
# command. Add two more commands to make karel: move(),
# pick_beeper(), move()
def main():
    move()
    pick_beeper()
    move()
    
    # add your code here

# don't edit these next two lines
# they tell python to run your main function
if __name__ == "__main__":
    main()
