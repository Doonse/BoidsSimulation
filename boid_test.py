import pygame as pg
from pygame import Vector2 as Vector
import random
from rules import Rules

class Boid:
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
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
        center = Vector(0, 0)
        for boid in boids:
            if boid.position != self.position:
                center += boid.position
        
        center = center / 100
        print(center)
        return (center - self.position) / 10
    

    def keep_distance_away(self, boids):
        distance = Vector(1000, 0)
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
        w1 = 0.4 # Rule1: Move towards the center of mass of neighbours
        w2 = 0.2 # Rule2: Keep a small distance away from other objects 
        w3 = 0.2 # Rule3: Try to match velocity with near boids
        w4 = 0 # Rule4: Tend to the palace

        # Find the center of the boids before applying the rules 
        n = self.neighbors(boids)
        cohesian = w1 * self.fly_towards_center(n)
        separation = w2 * self.keep_distance_away(n)
        alignment = w3 * self.match_velocity(n)

        self.velocity = self.velocity + cohesian + separation # + alignment

        self.velocity.scale_to_length(5)
        self.position += self.velocity
        self.wrap_position(boids)