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

    # Draw the hoiks on the screen
    def draw(self, screen):
        pg.draw.circle(screen, (255, 0, 0), self.position, 5)
    
    # Update the position of the hoiks
    def update(self, boids, hoiks):

        chase = Rules.chase(self, boids)
        efficiency = Rules.keep_distance_away(self, hoiks, 50) 
        align = Rules.match_velocity(self, boids)

        self.velocity += chase + efficiency + align

        self.velocity.scale_to_length(5)

        self.position += self.velocity

        Rules.wrap_position(self)
    






