from tkinter import *
import math
root = Tk()

canvas = Canvas(root, width = 400, height = 400)
canvas.pack()

def draw_circle(x, y, r):
    canvas.create_oval(x, y, x + 2 * r, y + 2 * r, fill="", outline="black")

def draw_fractal(x, y, r):
    if r < 10:
        return
    else:
        draw_circle(x, y, r),
        draw_fractal(x + r / 2, y, r / 2),
        draw_fractal(x, y + r * 2/3, r / 2),
        draw_fractal(x + r, y + r * 2/3, r / 2)


draw_fractal(5, 5, 196)


root.mainloop()