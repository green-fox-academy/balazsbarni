from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def draw_square(start_x, start_y):
    draw_box = canvas.create_rectangle(start_x, start_y, (start_x+50), (start_y+50))

draw_square(100, 150)

root.mainloop()