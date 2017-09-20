from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

red_line = canvas.create_line(100, 100, 200, 100, fill = "red")
pink_line = canvas.create_line(200, 100, 200, 200, fill = "pink")
yellow_line = canvas.create_line(200, 200, 100, 200, fill = "yellow")
green_line = canvas.create_line(100, 200, 100, 100, fill = "green")

# draw a box that has different colored lines on each edge.

root.mainloop()