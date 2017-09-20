from tkinter import *

root = Tk()
width = 300
height = 300
size = width/8
canvas = Canvas(root, width=str(width), height=str(height))
canvas.pack()

# fill the canvas with a checkerboard pattern.
def boxes_in_row(board_size):
    for line in range(8):
        for row in range (8):
            if (line+row) % 2 == 0:
                draw_box = canvas.create_rectangle(line*size, row*size, (line+1)*size, (row+1)*size, fill = "black")


boxes_in_row(size)
#draw_box = canvas.create_rectangle((b*width/8),((c+1)*width/8), ((b+1)*width/8),(c*width/8), fill="black")

root.mainloop()