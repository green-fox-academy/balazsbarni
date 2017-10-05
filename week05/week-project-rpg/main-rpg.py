from tkinter import *
import random

class Map(object):
    root = Tk()

    def __init__(self):
        self.size = 72
        self.canvas = Canvas(self.root, width = 900, height = 750)
        self.floor_image = PhotoImage(file = "floor.gif")
        self.wall_image = PhotoImage(file = "wall.gif")
        self.map_plan = [[0,0,0,1,0,1,0,0,0,0],
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

    def __init__(self, coord_x, coord_y, entity_image, canvas, health, attack, defense):
        self.entity = None
        self.size = 72
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.entity_image = entity_image
        self.canvas = canvas
        self.health = health
        self.attack = attack
        self.defense = defense

    def create_entity(self):
        x = self.coord_x * self.size + self.size/2
        y = self.coord_y * self.size + self.size/2
        self.entity = self.canvas.create_image(x, y, image = self.entity_image)
    
    def move(self, x, y):
        self.coord_x += x 
        self.coord_y += y
        self.canvas.move(self.entity, self.size * x , self.size * y)

    

class Hero(Entity):
    
    def __init__(self, canvas):
        self.hero_down = PhotoImage(file = "hero-down.gif")
        self.hero_up = PhotoImage(file = "hero-up.gif")
        self.hero_left = PhotoImage(file = "hero-left.gif")
        self.hero_right = PhotoImage(file = "hero-right.gif")
        self.d6 = random.randint(1, 6)
        self.hero_level = 1
        super().__init__(0, 0, self.hero_down, canvas, 20 + 3 * self.d6, 5 + self.d6, 2 * self.d6)
        self.size = 72
        self.hero = None

    def update_image(self, new_image, canvas):
        canvas.itemconfig(self.entity, image = new_image)


class Skeleton(Entity):

    def __init__(self, x, y, canvas):
        self.skeleton_image = PhotoImage(file = "skeleton.gif")
        self.d6 = random.randint(1, 6)
        super().__init__(x, y, self.skeleton_image, canvas, 2 * self.d6 + self.d6, self.d6, 1 / 2 * self.d6 + self.d6 / 2)
        self.size = 72
        self.skeleton = None

class Boss(Entity):

    def __init__(self, x, y, canvas):
        self.boss_image = PhotoImage(file = "boss.gif")
        self.d6 = random.randint(1, 6)
        self.boss_level = 1
        super().__init__(x, y, self.boss_image, canvas, 2 * self.boss_level * self.d6 + self.d6, self.boss_level * self.d6 + self.d6, self.boss_level / 2 * self.d6 + self.d6 / 2)
        self.size = 72
        self.boss = None
        

class Game(object):
  
    def __init__(self, skeleton_number):
        self.map = Map()
        self.map.draw_full_map()
        self.hero = Hero(self.map.canvas)
        self.hero.create_entity()
        self.npcs = []
        self.spawn_skeleton(skeleton_number)
        self.spawn_boss()
        self.size = 72
        self.map.root.bind("<KeyPress>", self.on_key_press)
        self.hud = self.map.canvas.create_text(800, 200, font="Times 20 italic bold", text = self.status(self.hero.health))
        self.map.canvas.pack()
        self.map.canvas.focus_set()
        self.map.root.mainloop()

    def spawn_skeleton (self, skeleton_number):
        initial_num = 1
        while initial_num <= skeleton_number:
            ran_x = random.randint(1, 9)
            ran_y = random.randint(1, 9)
            if self.map.get_cell(ran_x, ran_y) == True:
                skeli = Skeleton(ran_x, ran_y, self.map.canvas)
                skeli.create_entity()
                self.npcs.append(skeli)
                initial_num += 1

    def spawn_boss (self):
        initial_num = 0
        while initial_num < 1:
            ran_x = random.randint(5, 9)
            ran_y = random.randint(5, 9)
            if self.map.get_cell(ran_x, ran_y) == True:
                boss = Boss(ran_x, ran_y, self.map.canvas)
                boss.create_entity()
                self.npcs.append(boss)
                initial_num += 1


        

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
        self.battle()

    def battle(self):
        for i in range(len(self.npcs)):
            if self.npcs[i].coord_x == self.hero.coord_x and self.npcs[i].coord_y == self.hero.coord_y:
                while self.hero.health >= 0 or self.npcs[i].health >= 0:
                    current_hp = self.hero.health
                    current_npc = self.npcs[i].health
                    hr = random.randint(1,6)
                    if self.hero.attack  > self.npcs[i].defense:
                        print("belo")
                        current_npc -= self.hero.attack + (2 * hr)
                        if current_npc <= 0:
                            self.npcs[i].move(10, 10)
                            break
                    nr = random.randint(1,6)
                    if self.npcs[i].attack + (2 * nr) + 4 > self.hero.defense:
                        print("helo")
                        current_hp -= self.npcs[i].attack + (2 * hr)
                        self.map.canvas.itemconfig(self.hud, text = self.status(current_hp))
                        if current_hp <= 0:
                            self.map.canvas.create_text(800, 400, text = "GAME OVER")
                    self.hero.health = current_hp        
                    self.npcs[i].health = current_npc
                    

    def status (self, health):
        return "Hero (Level: " + str(self.hero.hero_level) + ") \nHP: " + str(health) + " \nAttack Point: " + str(self.hero.attack) + "  \nDefense Point: " + str(self.hero.defense)
        

game = Game(3)
