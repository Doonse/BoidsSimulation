import random
from pygame import Vector2
import pygame as pg
from rules import Rules

class Hoik(Rules):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.position = Vector2(random.randrange(0, screen_width), random.randrange(0, screen_height))
        self.velocity = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 100

    ### Draw the hoiks on the screen
    def draw(self, screen):
        pg.draw.circle(screen, (255, 0, 0), self.position, 5)
    
    ### Update the position of the hoiks
    def update(self, boids, hoiks):

        ### Weights of the rules. Attemt to make it more realistic
        w1 = 0.7 # Weight for chasing the closest boid
        w2 = 0.7 # Keep distance away from other hoiks 
        w3 = 0.5 # Match velocity

        ### Rules hoiks follow
        # Chase the closest boid
        chase = w1 * Rules.chase(self, boids) 

        # Keep distance away from other hoiks. Avoid collision and converging on each other
        efficiency = w2 * Rules.keep_distance_away(self, hoiks, 50) 

        # Match velocity 
        align = w3 * Rules.match_velocity(self, boids)

        # Update velocity
        self.velocity += chase + efficiency + align

        # Limit the speed of the hoiks 
        self.velocity.scale_to_length(5)

        # Update position
        self.position += self.velocity

        # Wrap the position of the hoiks
        Rules.wrap_position(self)
    






