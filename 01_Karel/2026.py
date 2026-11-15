"""
Assignment: 2026
Course: Stanford CS106A
Filename: 2026.py

Description:
A Karel the Robot program where Karel celebrates the year 2026 
by placing 20 beepers on the first stack, moving forward, placing 
26 beepers on|^{the} second stack, and moving one final step to the right.
"""

from karel.stanfordkarel import *

"""
When you finish writing this file, Karel should be able to 
place 20 beepers, then 26 beepers, and end facing East to 
the right of the 26 beepers.
"""


def main():
    # Place 20 beepers for the first digit stack, move forward,
    # place 26 beepers for the second stack, and take one final step.
    for i in range(20):
        put_beeper()
    move()
    for i in range(26):
        put_beeper()  
    move()    


if __name__ == '__main__':
    main()
