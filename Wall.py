#Code in form of a class

class Masonary:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height*self.width

def amount_count(self, wall):
    return brick.area()/ wall.area()
    

brick = Masonary(75, 225)
blockflat = Masonary(112.5, 450)
blockedge = Masonary(225, 450)


wall = Masonary(2700, 1800)
    

print(wall.area())
print(wall.area()/brick.area())
