from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    pass

    var x,y
    x = x0
    y = y0

    var A, B
    #FIX THIS -- WHAT ARE A AND B
    A = 0 #positive
    B = 0 #negative

    #octant 1
    d = 2A + B
    while x < x1:
        plot(x, y)
        if d < 0:
            y = y + 1
            d = d + 2B
        x = x + 1
        d = d + 2B
    #end of octant 1
