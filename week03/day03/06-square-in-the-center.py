from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a green 10x10 square to the center of the canvas.
width = 300
height = 300
orange_box = canvas.create_rectangle((width / 2 - 5), (height / 2 - 5), (width / 2 + 5), (height / 2 + 5), fill='orange')

root.mainloop()