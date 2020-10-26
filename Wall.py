#Code in form of a class

class Masonry:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height*self.width
 
brick = Masonry(75, 225)
blockflat = Masonry(112.5, 450)
blockedge = Masonry(225, 450)

class Wall(Masonry):
    def __init__(self, height, width):
        super().__init__(height, width)
    def __truediv__(self, other):
        return self.area/ other.area

sample = Wall(2700, 1800)
    

print(sample.area())
print(Wall.__truediv__(sample, brick))
#print(type(brick.area))