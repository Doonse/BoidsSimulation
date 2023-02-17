import pygame as pg
from pygame import Vector2 as Vector
import random
from rules import Rules

class Boid(Rules):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))

    # Draw the boids on the screen
    def draw(self, screen): 
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)

    # This is where the three rules are called, which move the boids
    def update(self, boids):
        self.velocity = self.velocity + Rules.fly_towards_center(self, boids) + Rules.keep_distance_away(self, boids) + Rules.match_velocity(self, boids)

        # Limit the velocity of the boids to 6 and update the position
        self.velocity.scale_to_length(6) 
        self.position += self.velocity
        
        
    # This function makes sure the boids wrap around the screen when they reach the edge
    def edge_wrap(self, width, height):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height
        

    
    
