from tkinter import *
import math
root = Tk()

canvas = Canvas(root, width = 450, height = 450)
canvas.pack()

def draw_hexagon(x, y, size):
    height = math.sqrt(3) / 2 * size
    canvas.create_polygon(x, y, x + size / 2, y - height,
                          x + size * 1.5, y - height,
                          x + size * 2, y,
                          x + size * 1.5, y + height,
                          x + size / 2, y + height,
                          fill="", outline="black")

def draw_fractal(x, y, size):
    height = math.sqrt(3) / 2 * size
    if size < 2:
        return
    else:
        draw_hexagon(x, y, size),
        draw_fractal(x, y, size / 3),
        draw_fractal(x + size * 2 / 6, y - height * 2 /3, size / 3),
        draw_fractal(x + size,  y - height * 2 /3, size / 3),
        draw_fractal(x + size + size / 3, y, size / 3),
        draw_fractal(x + size, y + height * 2 / 3, size / 3),
        draw_fractal(x + size * 2 / 6, y + height * 2 / 3, size / 3)


draw_fractal(10, 200, 200)

root.mainloop()