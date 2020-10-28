#Code in form of a class

class Masonry:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return int(self.height*self.width)
 
brick = Masonry(75, 225)
blockflat = Masonry(112.5, 450)
blockedge = Masonry(225, 450)

class Wall(Masonry):
    def __init__(self, height, width):
        super().__init__(height, width)

def solution(area1, area2):
    return int(area1.area()/ area2.area())


#sample wall, I named it sample as not to confuse it with the Wall class
sample = Wall(2700, 1800)
    

#These print statements are used to test if things are working.
#print(sample.area())
#print(brick.area())

#The brick count solution
print(solution(sample, brick))