from tkinter import *

root = Tk()

width = 300
height = 300
number_of_boxes = 7
bigger_from_step = 10
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()

def purple_steps (number_of_steps, bigger_each):
    x = 10
    y = 20
    box_size = 10
    for boxes in range(number_of_steps):
        draw_box = canvas.create_rectangle(x, x, y, y, fill="purple")
        box_size = x + bigger_from_step
        x = y
        y = box_size + x



purple_steps(number_of_boxes, bigger_from_step)

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

root.mainloop()