import pygame as pg
from pygame import Vector2 as Vector
import random
from rules import Rules

class Boid:
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = Vector(0, 0)
        self.width = width
        self.height = height
        self.max_speed = 5
        self.max_force = 0.1

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)

    def update(self, boids):
        self.acceleration += Rules.cohesion(self, boids) + Rules.separation(self, boids) + Rules.alignment(self, boids)
        self.velocity += self.acceleration
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
        

    
    
