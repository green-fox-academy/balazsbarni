from tkinter import *

root = Tk()
width = 300
height = 300
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def square_to_middle(square_size):
    draw_box = canvas.create_rectangle((width / 2 - square_size / 2), (height / 2 - square_size / 2), (width / 2 + square_size / 2), (height / 2 + square_size / 2))

square_to_middle(50)

root.mainloop()