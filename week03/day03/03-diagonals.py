from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

diagonal_first = canvas.create_line(0, 0, 300, 300, fill= "green" )
diagonal_second = canvas.create_line(0, 300, 300, 0, fill= "green" )
# draw the canvas' diagonals in green.

root.mainloop()