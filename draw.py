from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    #variables x,y
    x = x0
    y = y0

    #so x0 is always smaller than x1
    if(x0 > x1):
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #HORIZONTAL LINE
    if(y0 == y1):
        while(x <= x1):
            plot(screen, color, int(x), int(y))
            x = x + 1

    #VERTICAL LINE
    elif(x0 == x1):
        while(y <= y1):
            plot(screen, color, int(x), int(y))
            y = y + 1


    else:

        #SETUP
        #variables A, B
        A = y1 - y0 #positive
        B = -(x1 - x0) #negative

        #slope
        slope = (y1-y0)/(x1-x0)

        #OCTANT 1,5
        #if statement in octant 1,5
        if(slope < 1 and slope > 0):
            d = 2*A + B
            while x <= x1:
                plot(screen, color, int(x), int(y))
                if d > 0:
                    y = y + 1
                    d = d + 2*B
                x = x + 1
                d = d + 2*B


        #OCTANT 2,6
        #if statement in octant 2,6
        if(slope > 1):
            d = A + 2*B
            while y <= y1:
                plot(screen, color, int(x), int(y))
                if d < 0:
                    x = x + 1
                    d = d + 2*A
                y = y + 1
                d = d + 2*B


        #OCTANT 3, 7
        #if statement in octant 3,7
        if(slope < -1):
            d = A + 2*B
            while y >= y1:
                plot(screen, color, int(x), int(y))
                if d > 0:
                    x = x + 1
                    d = d - 2*A
                y = y - 1
                d = d - 2*B

        #OCTANT 4, 8
        #if statement in octant 4,8
        if(slope < 0 and slope > -1):
            d = 2*A + B
            while x <= x1:
                plot(screen, color, int(x), int(y))
                if d < 0:
                    y = y - 1
                    d = d - 2*B
                x = x + 1
                d = d + 2*A


        #NOT IN AN OCTANT
        #if slope is 1
        if(slope == 1):
            while x <= x1:
                plot(screen, color, int(x), int(y))
                x = x + 1
                y = y + 1

        #if slope is -1
        if(slope == -1):
            while x <= x1:
                plot(screen, color, int(x), int(y))
                x = x + 1
                y = y - 1
