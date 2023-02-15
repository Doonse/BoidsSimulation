from boid import Boid
import numpy as np


class Flock(Boid):
    # create a flock of boids with a center of mass
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.boids = []
        self.color = np.random.randint(0, 255, 3)
        self.vx = 1
        self.vy = 1

    def addBoid(self, boid):
        self.boids.append(boid)

    def update(self):
        for boid in self.boids:
            boid.update()

    def draw(self, screen):
        for boid in self.boids:
            boid.draw(screen)

    def getColor(self):
        return self.color
    
    def getPos(self):
        return (self.x, self.y)
    
    def getVel(self):
        return (self.vx, self.vy)