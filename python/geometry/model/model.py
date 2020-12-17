from functools import total_ordering
import math

@total_ordering
class Point2D:
    # methode object: 1er parametre l'objet courant
    def __init__(self, name=None, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        
    # override de __repr__ et __str__
    def __repr__(self):
        # old python: format % v1, v2, v3
        # return "{}({},{})".format(self.name, self.x, self.y)
        return f"{self.name}({self.x},{self.y})"
        
    # override default __eq__ based on memory address memory
    def __eq__(self, other):
        # choix de dev: isinstance, ...
        if type(other) != Point2D:
            return NotImplemented
        return (self.name, self.x, self.y) == (other.name, other.x, other.y)
    
    # ovverride default __lt__ (<) which returns NotImplemented
    def __lt__(self, other):
        if type(other) != Point2D:
            return NotImplemented
        return (self.x, self.y, self.name) < (other.x, other.y, other.name)
    
    # methode objet métier
    def distance(self, other):
        # check or not
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    # TODO: redefine also __hash__
    
    @staticmethod
    def fromString(pointString):
        # TODO: parsing
        return Point2D()

class Circle:
    pass