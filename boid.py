import pygame as pg
from pygame import Vector2 as Vector
import random
import math


class Boid:
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.width = width
        self.height = height

    def draw(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.position, 5)
    
    def cohesion(self, boids): # boids is a list of boids
        center = Vector(0, 0) # center is a vector
        for boid in boids: # boid in boids
            center += boid.position # add the position of the boid to the center vector
        center /= len(boids) # divide the center vector by the number of boids
        return (center - self.position) / 1000 # return the vector from the center of the boids to the boid

    def separation(self, boids):
        distance = Vector(0, 0)
        for boid in boids:
            if boid.position != self.position:
                distance += (self.position - boid.position) / (self.position.distance_to(boid.position) ** 4)
        return distance

    def alignment(self, boids):
        velocity = Vector(0, 0) 
        for boid in boids:
            velocity += boid.velocity
        velocity /= len(boids)
        return (velocity - self.velocity) / 8
    
    def edge_wrap(self, width, height):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height
        

    def update(self, boids):
        self.position += self.velocity
        self.velocity += self.cohesion(boids) + self.separation(boids) + self.alignment(boids)
        self.velocity.scale_to_length(2)
    


    
    
