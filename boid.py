# os
import os

# math
import math

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
        pg.draw.circle(screen, (80, 150, 100), (int(self.position.x), int(self.position.y)), 4)

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
