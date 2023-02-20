import random
import numpy as np
from pygame import Vector2 as Vector
import pygame as pg

class Hoik():
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 100

    # Draw the hoids on the screen
    def draw(self, screen):
        pg.draw.circle(screen, (255, 0, 0), self.position, 5)
    
    def my_food(self, hoiks):
        distance = Vector()
        for hoik in hoiks:
            if hoik.position != self.position:
                if (hoik.position - self.position).length() < 50:
                    distance = distance - (hoik.position - self.position)
        return distance

    def chase(self, boids):
        closest_boid = None
        closest_distance = 1000000
        for boid in boids:
            distance = abs(self.position.distance_to(boid.position))
            if distance < self.radius:
                closest_distance = distance
                closest_boid = boid
        if closest_boid:
            return (closest_boid.position - self.position).normalize()

        return Vector(0, 0)
       
    def wrap_position(self, screen_width, screen_height):
        if self.position.x > screen_width:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = screen_width
        if self.position.y > screen_height:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = screen_height



    def update(self, boids, hoiks):

        chase = self.chase(boids)
        efficiency = self.my_food(hoiks)

        self.velocity += chase + efficiency

        self.velocity.scale_to_length(5)

        self.position += self.velocity

        self.wrap_position(1200, 900)
    






