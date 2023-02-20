import pygame as pg
from pygame import Vector2
import random
from rules import Rules

class Boid(Rules):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.position = Vector2(random.uniform(0, screen_width), random.uniform(0, screen_height))
        self.velocity = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 100

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)

    def update(self, boids, hoiks):
        
        # Weights of the rules
        w1 = 0.2 # Rule1: Move towards the center of mass of neighbours
        w2 = 0.3 # Rule2: Keep a small distance away from other objects 
        w3 = 0.5 # Rule3: Try to match velocity with near boids

        # Neighbors in range
        n = Rules.neighbors(self, boids)

        # Rules to follow
        cohesian = w1 * Rules.fly_towards_center(self, n)
        separation = w2 * Rules.keep_distance_away(self, n)
        alignment = w3 * Rules.match_velocity(self, n)

        # Hoiks in range
        run = Rules.tend_to_place(self, hoiks) 

        # Update velocity 
        self.velocity += cohesian + separation + alignment + run

        # Limit the speed of the boids
        self.velocity.scale_to_length(5)

        # Update position
        self.position += self.velocity
        
        # Wrap the position of the boids
        Rules.wrap_position(self)