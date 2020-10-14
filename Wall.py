#Code in form of a class

class masonary:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

brick = masonary(75, 225)
blockflat = masonary(112.5, 450)
blockedge = masonary(225, 450)


wall = masonary(2700, 1800)

print(wall.area())
