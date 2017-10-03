from tkinter import *

root = Tk()
width = 750
height = 750
canvas = Canvas(root, width=str(width), height=str(height))

floor_image = PhotoImage(file = "floor.gif")
wall_image = PhotoImage(file = "wall.gif")
hero_down = PhotoImage(file = "hero-down.gif")
hero_up = PhotoImage(file = "hero-up.gif")
hero_left = PhotoImage(file = "hero-left.gif")
hero_right = PhotoImage(file = "hero-right.gif")



def draw_floor_piece(x, y, size):
    floor = canvas.create_image(x * size, y * size, image = floor_image, anchor = "nw")

def draw_wall_piece(x, y, size):  
    canvas.create_image(x * size, y * size, image = wall_image, anchor = "nw")

map_plan = [[0,0,0,1,0,1,0,0,0,0],
            [0,0,0,1,0,1,0,1,1,0],
            [0,1,1,1,0,1,0,1,1,0],
            [0,0,0,0,0,1,0,0,0,0],
            [1,1,1,1,0,1,1,1,1,0],
            [0,1,0,1,0,0,0,0,1,0],
            [0,1,0,1,0,1,1,0,1,0],
            [0,0,0,0,0,1,1,0,1,0],
            [0,1,1,1,0,0,0,0,1,0],
            [0,0,0,1,0,1,1,0,1,0]
            ]

def draw_full_map(x,y, size):
    for line in range(len(map_plan)):
        for row in range(len(map_plan)):
            if map_plan[line][row] == 0:
                draw_floor_piece(row, line, size)
            elif map_plan[line][row] == 1:
                draw_wall_piece(row, line, size)


def get_cell(x, y):
    for line in range(len(map_plan)):
        for row in range(len(map_plan)):
            if map_plan[x][y] == 0:
                return True
            else:
                return False


class Move_hero:
    def __init__(self):
        self.hero = None

    def create_hero(self, x, y, hero_image):
        self.hero = canvas.create_image(x, y, image = hero_image)

    def update_image(self, new_image):
        canvas.itemconfig(self.hero, image = new_image)
    

    def move(self, dx, dy):
        canvas.move(self.hero, dx, dy )

movehero = Move_hero()

draw_full_map(72, 72, 72)
movehero.create_hero(36, 36, hero_down)

def on_key_press(e):
    if e.keysym == 'Up':
        movehero.move(0, -72)
        movehero.update_image(hero_up)
    elif e.keysym == 'Down':
        movehero.move(0, 72)
        movehero.update_image(hero_down)
    elif e.keysym == 'Left':
        movehero.move(-72, 0)
        movehero.update_image(hero_left)
    elif e.keysym == 'Right':
        movehero.move(72, 0)
        movehero.update_image(hero_right)



root.bind("<KeyPress>", on_key_press)
canvas.pack()

canvas.focus_set()
root.mainloop()