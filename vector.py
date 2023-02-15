import numpy as np
import rules as rule

class Vector:
    # Boid vectors are 2D
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    
    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def mag(self):
        return np.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalize(self):
        return self / self.mag()
    
    