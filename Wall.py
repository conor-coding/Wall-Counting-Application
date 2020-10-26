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
    #Attempting to divide the sample wall area by the brick area
    def __truediv__(self, other):
        return self.area/ other.area

#sample wall, I named it sample as not to confuse it with the Wall class
sample = Wall(2700, 1800)
    
#This print statement is my bane. I can't work out the formula to divide two methods together.
print(Wall.__truediv__(sample, brick))
#These print statements are used to test if things are working.
#print(sample.area())
#print(brick.area())
