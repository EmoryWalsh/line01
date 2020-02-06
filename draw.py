from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    pass

    #variables x,y
    x = x0
    y = y0

    #variables A, B
    #FIX THIS -- WHAT ARE A AND B
    A = 0 #positive
    B = 0 #negative

    #############################################################
    #OCTANT 1

    #if statement in octant 1
    d = 2A + B
    while x < x1:
        plot(x, y)
        if d < 0:
            y = y + 1
            d = d + 2B
        x = x + 1
        d = d + 2B

    ###############################################################
