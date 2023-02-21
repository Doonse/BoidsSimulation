<<<<<<< HEAD
import pygame as pg
from pygame import Vector2
import random

class Boid:
    def __init__(self, screen_width, screen_height):
        self.position = Vector2(random.uniform(0, screen_width), random.uniform(0, screen_height))
        self.velocity = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 70

    # Draw the boids on the screen
    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)

    def neighbors(self, boids):
        neighbors = []
        for boid in boids:
            if boid.position != self.position:
                if self.position.distance_to(boid.position) < self.radius:
                    neighbors.append(boid)
        return neighbors

    def fly_towards_center(self, boids):
        center = Vector2(0, 0)
        for boid in boids:
            if boid.position != self.position:
                center += boid.position
        if len(boids) > 1:
            center = center / (len(boids) - 1)
            return (center - self.position) / 100
        return Vector2(0, 0)
    
    def keep_distance_away(self, boids):
        distance = Vector2()
        for boid in boids:
            if boid.position != self.position:
                if (boid.position - self.position).length() < 10:
                    distance = distance - (boid.position - self.position)
        return distance
    
    def match_velocity(self, boids):
        velocity = Vector2(0, 0)
        for boid in boids:
            if boid.position != self.position:
                velocity += boid.velocity
        if len(boids) > 1:
            velocity = velocity / (len(boids) - 1)
            return (velocity - self.velocity) / 8
        return Vector2(0, 0)

    def tend_to_place(self, boids):
        perceived_center = Vector2(0, 0)

        for boid in boids:
            if boid.position != self.position: 
                perceived_center += boid.position
        perceived_center = perceived_center / 100 
        return (perceived_center - self.position) / 1000

    def wrap_position(self, screen_width, screen_height):
        if self.position.x > screen_width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = screen_width
        if self.position.y > screen_height:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = screen_height

    # This is where the three rules are called, which move the boids
    def update(self, boids, screen_width, screen_height):
        # Weights of the rules
        w1 = 0.3 # Rule1: Move towards the center of mass of neighbours
        w2 = 0.2 # Rule2: Keep a small distance away from other objects 
        w3 = 0.4 # Rule3: Try to match velocity with near boids
        w4 = 0 # Rule4: Tend to the palace

        # Find the center of the boids before applying the rules 
        n = self.neighbors(boids)
        cohesian = w1 * self.fly_towards_center(n)
        separation = w2 * self.keep_distance_away(n)
        alignment = w3 * self.match_velocity(n)

        self.velocity = self.velocity + cohesian + separation + alignment 

        self.velocity.scale_to_length(5)
        self.position += self.velocity
        self.wrap_position(screen_width, screen_height)
=======
# Pygame
import pygame as pg
from pygame import Vector2
from pygame import sprite as sp

# Random number generator
import random

# Rules class
from rules import Rules


class Boid(Rules):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.position = Vector2(random.uniform(0, screen_width), random.uniform(0, screen_height))
        self.velocity = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 100

    # Draw the boid
    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)

    ### Update the position of the boid
    def update(self, boids, hoiks, obstacles=[]):
        
        ### Weights of the rules
        w1 = 0.2 # Rule1: Move towards the center of mass of neighbours
        w2 = 0.4 # Rule2: Keep a small distance away from other objects 
        w3 = 0.3 # Rule3: Try to match velocity with near boids
        w4 = 0.6 # Rule4: Avoid obstacles

        ### Neighbors in range
        n = Rules.neighbors(self, boids)

        ### Rules to follow
        cohesian = w1 * Rules.fly_towards_center(self, n)
        separation_from_boids = w2 * Rules.keep_distance_away(self, n, 9)
        alignment = w3 * Rules.match_velocity(self, n)
        dodge_hoiks = w4 * Rules.tend_to_place(self, hoiks)
        dodge_obs = w4 * Rules.tend_to_place(self, obstacles)


        # Update velocity 
        self.velocity += cohesian + separation_from_boids + dodge_hoiks + dodge_obs + alignment

        # Limit the speed of the boids
        self.velocity.scale_to_length(5)

        # Update position
        self.position += self.velocity
        
        # Wrap the position of the boids
        Rules.bound_position(self)
>>>>>>> b1a01d62027e570bffe284fe39d96d76d2c67ead
