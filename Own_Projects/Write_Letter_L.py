from karel.stanfordkarel import *

def main():
    draw_L()

# To draw L one is horizontal line and one is vertical
# 5 corners for horizontal and 4 for vertical incuding common one

def draw_L(): # to draw letter l
    draw_horizontal_line() # will contain 5 corners
    draw_vertical_line() # will contain 4 corners

def draw_horizontal_line():
    #pre: karel is on (1,1) and facing east
    #post: Karel is on (1,1) and facing east.karel has drawn  horizontal line
    turn_left()
    for i in range (4):
        paint_corner('yellow')
        move()
    # fenchpost problem 
    paint_corner ('yellow')
    turn_around()
    move_to_wall()
    turn_left()

def draw_vertical_line():
    #pre: karel is in (1,1) facing east
    #post: karel is on (1,1) facing east while copleted drawing vertical line
    for i in range(3):
        paint_corner('yellow')
        move()
    #fenchpost problem
    paint_corner('yellow')
    turn_around()
    move_to_wall()
    turn_around()

def turn_around(): # turn back
    for i in range (2):
        turn_left()

def  move_to_wall():  #defining move_to_wall
    while front_is_clear():
        move()



# don't change this code
if __name__ == '__main__':
    main()
