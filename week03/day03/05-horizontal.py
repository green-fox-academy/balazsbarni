from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.
par_x = 100
par_y = 200

def draw_horizontal_from_start(par_first, par_second):
    horizontal_line = canvas.create_line(par_first,  par_second, (par_first + 50), par_second)

draw_horizontal_from_start(par_x, par_y)

root.mainloop()