import pygame as pg
from pygame import Vector2 as Vector
import random
from rules import Rules

class Boid:
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y) # Position vector
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1)) # Velocity vector
        self.acceleration = Vector(0, 0) # Acceleration vector
        self.width = width # Width of the screen
        self.height = height # Height of the screen
        self.max_speed = 5 # Maximum speed of the boids

    def draw(self, screen): # Draw the boids on the screen
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)

    def update(self, boids): # This is where the three rules are called, which move the boids
        self.velocity = self.velocity + Rules.cohesion(self, boids) + Rules.separation(self, boids) + Rules.alignment(self, boids)
        self.velocity.scale_to_length(5)
        self.position += self.velocity
    
    def edge_wrap(self, width, height):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height
        

    
    
