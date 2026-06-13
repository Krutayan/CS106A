"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    while front_is_clear():
        if left_is_clear():
            ascend_zigzag()
        else:
            descend_zigzag()
    
    go_to_final_spot() # for karel to come at 1st row of  last column while facing east

def ascend_zigzag():
    #pre: at 1st row and odd column facing east
    #post: at 2nd and even column facing east
    # all this and karel also puts beepers zig zag
    put_beeper()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()


def descend_zigzag():
    #pre: at 2nd row and odd column facing east
    #post: at 1st row and even column facing east
    # karel does not put beepers while descending
    move()
    turn_right()
    move()
    turn_left()

def go_to_final_spot(): #for coming in final spot
    turn_right()
    move()
    turn_left()

def turn_right(): # deriving right command using left command
    for i in range (3):
        turn_left()

    




        
   
    """
    Places beepers in a zig zag pattern.
    """
    


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
