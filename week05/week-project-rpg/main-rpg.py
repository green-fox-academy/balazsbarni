from tkinter import *

root = Tk()
width = 750
height = 750
size = 72
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
            [0,1,0,1,0,1,1,0,0,0],
            [0,0,0,0,0,1,1,0,1,0],
            [0,1,1,1,0,0,0,0,1,0],
            [0,0,0,1,0,1,1,0,0,0]
            ]

def draw_full_map():
    for line in range(len(map_plan)):
        for row in range(len(map_plan)):
            if map_plan[line][row] == 0:
                draw_floor_piece(row, line, size)
            elif map_plan[line][row] == 1:
                draw_wall_piece(row, line, size)


def get_cell(x, y):
    if 0 <= x <= 9 and 0 <= y <= 9:
        if map_plan[y][x] == 0:
            return True
        
class Hero:
    def __init__(self):
        self.hero = None
        self.coord_x = 0
        self.coord_y = 0

    def create_hero(self):
        x = size/2
        y = size/2
        self.hero = canvas.create_image(x, y, image = hero_down)

    def update_image(self, new_image):
        canvas.itemconfig(self.hero, image = new_image)
    
    def move(self, x, y):
        self.coord_x += x 
        self.coord_y += y
        canvas.move(self.hero, size * x , size * y)


hero = Hero()
draw_full_map()
hero.create_hero()


def on_key_press(e):
    if e.keysym == 'Up' and get_cell(hero.coord_x, hero.coord_y-1) == True:
        hero.move(0, -1)
        hero.update_image(hero_up)
    elif e.keysym == 'Down' and get_cell(hero.coord_x, hero.coord_y+1) == True:
        hero.move(0, 1)
        hero.update_image(hero_down)
    elif e.keysym == 'Left' and get_cell(hero.coord_x-1, hero.coord_y) == True:
        hero.move(-1, 0)
        hero.update_image(hero_left)
    elif e.keysym == 'Right' and get_cell(hero.coord_x+1, hero.coord_y) == True:
        hero.move(1, 0)
        hero.update_image(hero_right)



root.bind("<KeyPress>", on_key_press)
canvas.pack()

canvas.focus_set()
root.mainloop()