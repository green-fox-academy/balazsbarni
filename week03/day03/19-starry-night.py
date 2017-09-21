from tkinter import *
import random

root = Tk()
width = 300
height = 300
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack(fill="both", expand=True)
canvas.config(bg="black")


# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)
root["bg"] = "black"

for stars in range(100):
    x = random.randrange(width)
    y = random.randrange(width)
    canvas.create_rectangle(x, y, x+5, y+5, fill="yellow" )



root.mainloop()