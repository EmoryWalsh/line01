from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    if(x0 > x1):
        print(str(x0) + "," + str(y0))
        print(str(x1) + "," + str(y1))
        storx = x1
        x1 = x0
        x0 = storx
        story = y1
        y1 = y0
        y0 = story
        print(str(x0) + "," + str(y0))
        print(str(x1) + "," + str(y1))

    #############################################################
    #HORIZONTAL LINE
    #if(y0 === y)

    #variables x,y
    x = x0
    y = y0

    #variables A, B
    #FIX THIS -- WHAT ARE A AND B
    A = y1 - y0 #positive
    B = -(x1 - x0) #negative

    #############################################################
    #OCTANT 1

    #if statement in octant 1
    d = 2*A + B
    while x < x1:
        plot(screen, color, int(x), int(y))
        if d < 0:
            y = y + 1
            d = d + 2*B
        x = x + 1
        d = d + 2*B

    ###############################################################
