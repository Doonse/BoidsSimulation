import pygame as pg
from pygame import Vector2
import random

class Boid:
    def __init__(self, screen_width, screen_height):
        self.position = Vector2(random.uniform(0, screen_width), random.uniform(0, screen_height))
        self.velocity = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 100

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
            return (center - self.position) / 100
        return Vector2(0, 0)
    
    def keep_distance_away(self, boids):
        distance = Vector2()
        for boid in boids:
            if boid.position != self.position:
                if (boid.position - self.position).length() < 9:
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


    def tend_to_place(self, hoiks):
        run = Vector2(0, 0)
        for hoik in hoiks:
            if (hoik.position - self.position).length() < self.radius:
                run =  - (hoik.position - self.position).normalize()
        return run




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
    def update(self, boids, screen_width, screen_height, hoiks):
        # Weights of the rules
        w1 = 0.2 # Rule1: Move towards the center of mass of neighbours
        w2 = 0.3 # Rule2: Keep a small distance away from other objects 
        w3 = 0.5 # Rule3: Try to match velocity with near boids

        # Neighbors in range
        n = self.neighbors(boids)

        # Rules to follow
        cohesian = w1 * self.fly_towards_center(n)
        separation = w2 * self.keep_distance_away(n)
        alignment = w3 * self.match_velocity(n)

        # Hoiks in range
        run = self.tend_to_place(hoiks) 

        # Update velocity 
        self.velocity += cohesian + separation + alignment + run

        # Limit the speed of the boids
        self.velocity.scale_to_length(5)

        # Update position
        self.position += self.velocity
        
        # Wrap the position of the boids
        self.wrap_position(screen_width, screen_height)