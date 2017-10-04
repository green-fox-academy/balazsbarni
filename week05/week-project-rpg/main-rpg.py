from tkinter import *
import random

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

    def __init__(self, coord_x, coord_y, entity_image, canvas):
        self.entity = None
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.entity_image = entity_image
        self.canvas = canvas

    def create_entity(self):
        x = self.coord_x * self.size + self.size/2
        y = self.coord_y * self.size + self.size/2
        self.entity = self.canvas.create_image(x, y, image = self.entity_image)
    
    def move(self, x, y):
        self.coord_x += x 
        self.coord_y += y
        self.canvas.move(self.entity, self.size * x , self.size * y)

    

class Hero(Entity):
    size = 72
    hero_down = PhotoImage(file = "hero-down.gif")
    hero_up = PhotoImage(file = "hero-up.gif")
    hero_left = PhotoImage(file = "hero-left.gif")
    hero_right = PhotoImage(file = "hero-right.gif")
    
    def __init__(self, canvas):
        super().__init__(0, 0, self.hero_down, canvas)
        self.hero = None

    def update_image(self, new_image, canvas):
        canvas.itemconfig(self.entity, image = new_image)


class Skeleton(Entity):
    size = 72
    skeleton_image = PhotoImage(file = "skeleton.gif")

    def __init__(self, x, y, canvas):
        super().__init__(x, y, self.skeleton_image, canvas)
        self.skeleton = None

class Boss(Entity):
    size = 72
    boss_image = PhotoImage(file = "boss.gif")

    def __init__(self, x, y, canvas):
        super().__init__(x, y, self.boss_image, canvas)
        self.boss = None

class Game(object):
    map = Map()
    map.draw_full_map()
    size = 72
    hero = Hero(map.canvas)
    skeli1 = Skeleton(1, 1, map.canvas)
    skeli2 = Skeleton(1, 2, map.canvas)
    skeli3 = Skeleton(1, 3, map.canvas)
    boss = Boss(2, 1, map.canvas)
    hero.create_entity()
    skeli1.create_entity()
    skeli2.create_entity()
    skeli3.create_entity()
    boss.create_entity()

    def __init__(self):
        self.map.root.bind("<KeyPress>", self.on_key_press)
        self.map.canvas.pack()
        self.map.canvas.focus_set()
        self.map.root.mainloop()

    def on_key_press(self, e):
        if e.keysym == 'Up' and self.map.get_cell(self.hero.coord_x, self.hero.coord_y-1) == True:
            self.hero.move(0, -1)
            self.hero.update_image(self.hero.hero_up, self.map.canvas)
        elif e.keysym == 'Down' and self.map.get_cell(self.hero.coord_x, self.hero.coord_y+1) == True:
            self.hero.move(0, 1)
            self.hero.update_image(self.hero.hero_down, self.map.canvas)
        elif e.keysym == 'Left' and self.map.get_cell(self.hero.coord_x-1, self.hero.coord_y) == True:
            self.hero.move(-1, 0)
            self.hero.update_image(self.hero.hero_left, self.map.canvas)
        elif e.keysym == 'Right' and self.map.get_cell(self.hero.coord_x+1, self.hero.coord_y) == True:
            self.hero.move(1, 0)
            self.hero.update_image(self.hero.hero_right, self.map.canvas)


game = Game()