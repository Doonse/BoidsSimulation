import pygame as pg
from pygame import Vector2 as Vector
import random
from rules import Rules

class Boid:
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))

    # Draw the boids on the screen
    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)

    def fly_towards_center(self, boids):
        perceived_center = Vector(0, 0)

        for boid in boids:
            if boid.position != self.position: 
                perceived_center += boid.position 
        perceived_center = perceived_center / 100 
        return (perceived_center - self.position) / 1000


    def keep_distance_away(self, boids):
        distance = Vector(0, 0)
        for boid in boids:
            if boid.position != self.position:
                if self.position.distance_to(boid.position) < 10:
                    distance = distance - (boid.position - self.position)
        return distance
    

    def match_velocity(self, boids):
        velocity = Vector(0, 0)
        for boid in boids:
            if boid.position != self.position:
                velocity += boid.velocity
        velocity = velocity / 100
        return (velocity - self.velocity) / 8

    def tend_to_place(self, boids):
        perceived_center = Vector(0, 0)

        for boid in boids:
            if boid.position != self.position: 
                perceived_center += boid.position 
        perceived_center = perceived_center / 100 
        return (perceived_center - self.position) / 1000

    def wrap_position(self, boids):
        if self.position.x > 1200:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = 1200
        if self.position.y > 900:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = 900

    # This is where the three rules are called, which move the boids
    def update(self, boids):
        # Weights of the rules
        w1 = 1 # Rule1: Move towards the center of mass of neighbours
        w2 = 0.1 # Rule2: Keep a small distance away from other objects 
        w3 = 0.3 # Rule3: Try to match velocity with near boids
        w4 = 1 # Rule4: Tend to the palace

        # Find the center of the boids before applying the rules 

        self.velocity += self.fly_towards_center(boids) * w1  + self.keep_distance_away(boids) * w2 + self.match_velocity(boids) * w3 + self.tend_to_place(boids) * w4

        self.velocity.scale_to_length(5)
        self.position += self.velocity
        self.wrap_position(boids)
    





    # Anti-flocking behaviour
    # Negate the first rule (moving towards the centre of mass of neighbours)
    def anti_flock(self, boids):
        pass

