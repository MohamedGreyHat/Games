from math import hypot
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Vector(%r, %r)"%(self.x, self.y)
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    def __len__(self):
        return 2
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

x = input("x = ")      
y = input("y = ")

v = Vector2D(x, y)
print v 
print v * 3
print v + Vector2D(1, 1)
print abs(v)

