from tkinter import *

root = Tk()

canvas = Canvas(root, width='400', height='400', bg="yellow")
canvas.pack()

def draw_cube(x,y, size):
    canvas.create_rectangle(x, y, x+size, y+size, fill="")

def draw_fractal(x, y, size):
    if size < 2:
        return
    else:
        draw_cube(x, y, size),
        draw_fractal(x, y + size / 3, size / 3),
        draw_fractal(x + size / 3, y, size / 3),
        draw_fractal(x + 2 / 3 * size, y + size / 3, size / 3),
        draw_fractal(x + size / 3, y + 2 / 3 * size, size / 3)


draw_fractal(5, 5, 395)

root.mainloop()