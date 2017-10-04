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

class Entity(object):
    size = 72
    def __init__(self, coord_x, coord_y, entity_image):
        self.entity = None
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.entity_image = entity_image


    def create_entity(self):
        x = self.coord_x * self.size + self.size/2
        y = self.coord_y * self.size + self.size/2
        self.entity = Map.canvas.create_image(x, y, image = self.entity_image)
    
    def move(self, x, y):
        self.coord_x += x 
        self.coord_y += y
        Map.canvas.move(self.entity, self.size * x , self.size * y)

    

class Hero(Entity):
    size = 72
    hero_down = PhotoImage(file = "hero-down.gif")
    hero_up = PhotoImage(file = "hero-up.gif")
    hero_left = PhotoImage(file = "hero-left.gif")
    hero_right = PhotoImage(file = "hero-right.gif")
    
    def __init__(self):
        self.hero = None
        super().__init__(0, 0, self.hero_down)

    def update_image(self, new_image):
        Map.canvas.itemconfig(self.hero, image = new_image)

class Skeleton(Entity):
    size = 72
    skeleton_image = PhotoImage(file = "skeleton.gif")

    def __init__(self):
        self.skeleton = None
        self.skeleton_x = 1
        self.skeleton_y = 1
        super().__init__(self.skeleton_x, self.skeleton_y, self.skeleton_image)

class Boss(Entity):
    size = 72
    boss_image = PhotoImage(file = "boss.gif")

    def __init__(self):
        self.boss = None
        self.boss_x = 1
        self.boss_y = 0
        super().__init__(self.boss_x, self.boss_y, self.boss_image)




hero = Hero()
skeli = Skeleton()
boss = Boss()
map = Map()
map.draw_full_map()
hero.create_entity()
skeli.create_entity()
boss.create_entity()


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