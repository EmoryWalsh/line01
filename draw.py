from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    #SETUP
    if(x0 > x1):
        storex = x1
        x1 = x0
        x0 = storex
        storey = y1
        y1 = y0
        y0 = storey

    #variables x,y
    x = x0
    y = y0

    #############################################################
    #HORIZONTAL LINE
    if(y0 == y1):
        while(x < x1):
            plot(screen, color, int(x), int(y))
            x = x + 1

    #VERTICAL LINE
    if(x0 == x1):
        while(y < y1):
            plot(screen, color, int(x), int(y))
            y = y + 1


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
