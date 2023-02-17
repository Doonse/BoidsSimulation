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
        # Weights of the rules
        w1 = 10 # Rule1: Move towards the center of mass of neighbours
        w2 = 10 # Rule2: Keep a small distance away from other objects 
        w3 = 10 # Rule3: Try to match velocity with near boids
        w4 = -1 # Rule4: Tend to the palace

        # Find the center of the boids before applying the rules 

        c = Rules.find_center(self, boids)
        r1 = self.fly_towards_center(boids, c) * w1
        for boid in boids:
            boid.velocity += r1 + self.keep_distance_away(boid) * w2 + self.match_velocity(boid) * w3 # + self.tend_to_place(boid) * w4

            boid.velocity.scale_to_length(1)
            boid.position += boid.velocity / 10

    # Bounding the position of the boids to the screen so they don't fly off        
    def bound_position(self, boids):
        Xmin, Xmax, Ymin, Ymax = 0, 750, 0, 550 # Set the boundaries of the screen 
        vec = Vector(0, 0) # Initialize the vector to 0

        for boid in boids:
            if boid.position != self.position:
                if self.position.x < Xmin:
                    vec.x += 1 
                elif self.position.x > Xmax:
                    vec.x -= 1
                if self.position.y < Ymin:
                    vec.y += 1
                elif self.position.y > Ymax:
                    vec.y -= 1
                
        return vec
    
    def wrap_position(self, boids):
        # wrap around the screen
        if self.position.x > 800:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = 800
        if self.position.y > 600:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = 600




    # Anti-flocking behaviour
    # Negate the first rule (moving towards the centre of mass of neighbours)
    def anti_flock(self, boids):
        pass

