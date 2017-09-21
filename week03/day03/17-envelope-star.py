from tkinter import *

root = Tk()
width = 300
height = 300
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()
half = int(width/2)
# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

for line in range (0, half, 20):
    line_dr = canvas.create_line(line, half, half, half-line, fill= "green")

for line in range (0, half, 20):
    line_dr = canvas.create_line(half, line, half+line, half, fill= "green")

for line in range (0, half, 20):
    line_dr = canvas.create_line(line, half, half, half+line, fill= "green")

for line in range (0, half, 20):
    line_dr = canvas.create_line(half+line, half, half, half*2-line, fill= "green")
root.mainloop()