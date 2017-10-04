from tkinter import *

class Map(object):
    root = Tk()
    size = 72
    canvas = Canvas(root, width = 750, height = 750)
    floor_image = PhotoImage(file = "floor.gif")
    wall_image = PhotoImage(file = "wall.gif")
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

    def __init__(self):
        pass

    def draw_floor_piece(self, x, y, size):
        self.canvas.create_image(x * self.size, y * self.size, image = self.floor_image, anchor = "nw")

    def draw_wall_piece(self, x, y, size):  
        self.canvas.create_image(x * self.size, y * self.size, image = self.wall_image, anchor = "nw")

    def draw_full_map(self):
        for line in range(len(self.map_plan)):
            for row in range(len(self.map_plan)):
                if self.map_plan[line][row] == 0:
                    self.draw_floor_piece(row, line, self.size)
                elif self.map_plan[line][row] == 1:
                    self.draw_wall_piece(row, line, self.size)

    def get_cell(self, x, y):
        if 0 <= x <= 9 and 0 <= y <= 9:
            if self.map_plan[y][x] == 0:
                return True
        
class Hero:
    size = 72
    hero_down = PhotoImage(file = "hero-down.gif")
    hero_up = PhotoImage(file = "hero-up.gif")
    hero_left = PhotoImage(file = "hero-left.gif")
    hero_right = PhotoImage(file = "hero-right.gif")
    
    def __init__(self):
        self.hero = None
        self.coord_x = 0
        self.coord_y = 0

    def create_hero(self):
        x = self.size/2
        y = self.size/2
        self.hero = Map.canvas.create_image(x, y, image = self.hero_down)

    def update_image(self, new_image):
        Map.canvas.itemconfig(self.hero, image = new_image)
    
    def move(self, x, y):
        self.coord_x += x 
        self.coord_y += y
        Map.canvas.move(self.hero, self.size * x , self.size * y)


hero = Hero()
map = Map()
map.draw_full_map()
hero.create_hero()


def on_key_press(e):
    if e.keysym == 'Up' and map.get_cell(hero.coord_x, hero.coord_y-1) == True:
        hero.move(0, -1)
        hero.update_image(hero.hero_up)
    elif e.keysym == 'Down' and map.get_cell(hero.coord_x, hero.coord_y+1) == True:
        hero.move(0, 1)
        hero.update_image(hero.hero_down)
    elif e.keysym == 'Left' and map.get_cell(hero.coord_x-1, hero.coord_y) == True:
        hero.move(-1, 0)
        hero.update_image(hero.hero_left)
    elif e.keysym == 'Right' and map.get_cell(hero.coord_x+1, hero.coord_y) == True:
        hero.move(1, 0)
        hero.update_image(hero.hero_right)



Map.root.bind("<KeyPress>", on_key_press)
Map.canvas.pack()

Map.canvas.focus_set()
Map.root.mainloop()