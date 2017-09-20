from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
orange_box = canvas.create_rectangle(10, 10, 50, 50, fill= "orange")
tomato_box = canvas.create_rectangle(120, 100, 250, 200, fill= "tomato")
blue_box = canvas.create_rectangle(50, 200, 120, 250, fill= "blue")
black_box = canvas.create_rectangle(55, 55, 130, 120, fill= "black")

root.mainloop()