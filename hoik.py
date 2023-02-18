import random
from pygame import Vector2 as Vector
import pygame as pg
from boid import Boid

class Hoid(Boid):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 100

    # Draw the hoids on the screen
    def draw(self, screen):
        pg.draw.circle(screen, (255, 0, 0), self.position, 5)

    def update(self, correct):
        self.velocity = self.velocity + correct
        
        # Limit the velocity of the hoids to 5 and update the position
        self.velocity.scale_to_length(6)
        self.position += self.velocity
    
    def chase(self, boids):
        for boid in boids:
            if boid.position != self.position:
                if self.position.distance_to(boid.position) < self.radius:
                    self.position = boid.position
                    





    # Bounding the position of the hoids to the screen so they don't fly off        
    def bound_position(self, hoids):
        Xmin, Xmax, Ymin, Ymax = 100, 700, 100, 500 # Set the boundaries of the screen 
        vec = Vector(0, 0)

        for hoid in hoids:
            if hoid.position != self.position:
                if self.position.x < Xmin:
                    vec.x += 1 
                elif self.position.x > Xmax:
                    vec.x -= 1
                if self.position.y < Ymin:
                    vec.y += 1
                elif self.position.y > Ymax:
                    vec.y -= 1
                
        return vec

    def chase(self, boids):
        pass
