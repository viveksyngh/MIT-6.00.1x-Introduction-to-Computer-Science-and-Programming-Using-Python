class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self, other) :
        if self.x == other.x and self.y == other.y :
            return True
        else :
            return False
            
    def __repr__(c) :
        return 'Coordinate(c.getX(), c.getY())'

c = Coordinate(7, 8)
print c
c1 = Coordinate(7, 8) 
print c == c1
print eval(repr(c))

