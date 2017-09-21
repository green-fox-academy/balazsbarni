from tkinter import *

root = Tk()
width = 300
height = 300
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()

for line in range (0, width, 20):
    line = canvas.create_line(line, 0, width, line, fill="purple")

for line in range (0, height, 20):
    line = canvas.create_line(0, line, line, width, fill="green")

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

root.mainloop()