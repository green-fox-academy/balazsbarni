from tkinter import *

root = Tk()

width = 300
height = 300
number_of_boxes = 20
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()

def purple_steps (number_of_steps):
    for boxes in range(2,number_of_steps):
         draw_box = canvas.create_rectangle((10* boxes), (10 * boxes) , (10 * boxes +10) , (10 * boxes + 10), fill="purple")


purple_steps(number_of_boxes)

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]


root.mainloop()