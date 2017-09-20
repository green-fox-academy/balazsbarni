from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.
width = 300
height = 300
x_one, x_two = 280, 10
y_one, y_two = 120, 50
z_one, z_two = 200, 250

def line_draw_to_centre(par_one, par_two):
    line_to_center = canvas.create_line(par_one, par_two, width/2, height/2)

#line_first = canvas.create_line(x_one, x_two, (width / 2), (height / 2))
#line_second = canvas.create_line(y_one, y_two, 150, 150)
#line_third = canvas.create_line(z_one, z_two, 150, 150)

line_draw_to_centre(x_one, x_two)
line_draw_to_centre(y_one,y_two)
line_draw_to_centre(z_one, z_two)
root.mainloop()