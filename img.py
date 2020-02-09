from display import *
from draw import *

s = new_screen()

c1 = [250, 200, 2]
c2 = [50, 20, 0]
c3 = [200, 100, 250]
c4 = [250, 150, 150]
for x in range(100):
    draw_line(XRES/6 + 3*x, YRES/2 - 3*x, 5*XRES/6 - 3*x, YRES/2 + 3*x,s, c1)
    c1[0] -= 2
    c1[2] += 2
    draw_line(XRES/6 - 3*x, YRES/2 - 3*x, 5*XRES/6 + 3*x, YRES/2 + 3*x,s, c2)
    c2[0] += 2
    c2[1] += 2
    draw_line(XRES/6 - 3*x, YRES/2 + 3*x, 5*XRES/6 + 3*x, YRES/2 - 3*x,s, c3)
    c3[0] -= 2
    c3[2] -= 2
    draw_line(XRES/6 + 3*x, YRES/2 + 3*x, 5*XRES/6 - 3*x, YRES/2 - 3*x,s, c4)
    c4[1] -= 1
    c4[2] -= 1

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
