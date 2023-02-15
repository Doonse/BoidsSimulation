import numpy as np
import pygame as pg

class Boid:
    
    def __init__(self, x, y): # x, y, vx, vy, ax, ay, color 
        self.x = x # x position
        self.y = y # y position
        self.vx = 1 # Constant velocity in x direction
        self.vy = 1 # Constant velocity in y direction
        self.color = np.random.randint(0, 255, 3) # Random color

    def update(self): # update position and velocity
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        print(self.x, self.y)
        print(self.color)
        print(self.vx, self.vy)
        pg.draw.polygon(screen, self.color, [(self.x, self.y), (self.x + 10, self.y - 10), (self.x + 10, self.y)], 0)

    def getColor(self):
        return self.color
    
    def getPos(self):
        return (self.x, self.y)
    
    def getVel(self):
        return (self.vx, self.vy)
    