from tkinter import *

root = Tk()

width = 300
height = 300
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def draw_line_to_center (par_x, par_y):
    line_to_center = canvas.create_line(par_x, par_y, width/2, height/2)


for line in range(0, width, 20):
    for row in range(0, height, 20):
        draw_line_to_center(line, height)
        draw_line_to_center(height, row)
        draw_line_to_center(line, 0)
        draw_line_to_center(0, row)
        
        



#draw_line_to_center(32,55)

root.mainloop()