from tkinter import *
import random

root = Tk()
width = 300
height = 300
square_size = 250
square_number = 15
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def colored_square_to_middle(square_size, fill_color):
    draw_box = canvas.create_rectangle((width / 2 - square_size / 2), (height / 2 - square_size / 2), (width / 2 + square_size / 2), (height / 2 + square_size / 2), fill=fill_color)



def hex_code_colors():
    a = hex(random.randrange(0,256))
    b = hex(random.randrange(0,256))
    c = hex(random.randrange(0,256))
    a = a[2:]
    b = b[2:]
    c = c[2:]
    if len(a)<2:
        a = "0" + a
    if len(b)<2:
        b = "0" + b
    if len(c)<2:
        c = "0" + c
    z = a + b + c
    return "#" + z.upper()



for squares in range(1, square_number):
    colored_square_to_middle(square_size, hex_code_colors())
    square_size -= 20



root.mainloop()
