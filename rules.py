import numpy as np
from pygame import Vector2 as Vector
import random

class Rules:
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.width = width
        self.height = height
    
    def cohesion(self, boids):
        center = Vector(0, 0)
        for boid in boids:
            center += boid.position
        center /= len(boids)
        return 0.2 * (center - self.position) / 100
    
    def separation(self, boids):
        distance = Vector(0, 0)
        for boid in boids:
            if boid.position != self.position:
                distance += 0.1 * (self.position - boid.position) / (self.position.distance_to(boid.position) ** 4)
        return distance
    
    def alignment(self, boids):
        velocity = Vector(0, 0) 
        for boid in boids:
            velocity += boid.velocity
        velocity /= len(boids)
        return  0.1 * (velocity - self.velocity) / 8
    
    

