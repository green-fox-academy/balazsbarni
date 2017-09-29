#### Sharpie Set
#- Reuse your `Sharpie` class
#- Create `SharpieSet` class
#  - it contains a list of Sharpie
#  - count_usable() -> sharpie is usable if it has ink in it
#  - remove_trash() -> removes all unusable sharpies

class Sharpie(object):
    def __init__(self, color, width, ink):
        self.color = color
        self.width = width
        self.ink = ink

    def use(self):
        self.ink_amount -=1

    def __repr__(self):
        return '[{}, {}, {}]'.format(self.color, self.width, self.ink)

class SharpieSet(object):
    def __init__(self):
        self.sharpie = [Sharpie("red", 0.25, 5), Sharpie("blue", 0.5, 3)]

    def usable(self):
        counter = 0
        for items in sharpieset:
            print(items)


    


sharpieset = SharpieSet()
sharpieset.usable()
print(sharpieset.sharpie)