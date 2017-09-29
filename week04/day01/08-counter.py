class Counter(object):

    def __init__(self, value=0):
        self.value = value

    def add(self, to_add=1):
        self.value += to_add

    def get(self):
        return self.value
    
    def reset(self, value=0):
        self.value = value


nr = Counter()
print(nr.value)
nr.add(6)
nr.reset()
print(nr.get())