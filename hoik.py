# Pygame 
from pygame import Vector2
import pygame as pg

# Random
import random

# Rules class
from rules import Rules


class Hoik(Rules):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.position = Vector2(random.randrange(0, screen_width), random.randrange(0, screen_height))
        self.velocity = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.radius = 100 # Radius of the hoiks vision
        self.size = 5 # Size of the hoiks

    ### Draw the hoiks on the screen
    def draw(self, screen):
        pg.draw.circle(screen, (255, 0, 0), self.position, self.size)

    # Gain size when eating boids
    def grow(self, boids):
        for boid in boids:
            if (boid.position - self.position).length() < self.size + 2: # + 2 for extra reach
                self.size += 1 # Gain size
            if self.size > 20:
                self.size = 20 # Max size

    # Lose size when not eating boids for a while 
    def shrink(self):
        self.size -= 0.01 # Lose size continuously
        if self.size < 5: # Min size
            self.size = 5 

    def reproduce(self, hoiks):
        if len(hoiks) < 10:
            if self.size > 10:
                if random.random() < 0.1:
                    # Reproduce a new hoik next to the parent without overlapping and crashin the game
                    hoiks.append(Hoik(self.screen_width, self.screen_height))
                    hoiks[-1].position = self.position + Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

    def die(self, hoiks):
        if len(hoiks) > 2:
            if self.size < 6:
                if random.random() < 0.01:
                    hoiks.remove(self)


    

    
    ### Update the position of the hoiks
    def update(self, boids, hoiks):

        ### Weights of the rules. Attemt to make it more realistic
        w1 = 0.7 # Weight for chasing the closest boid
        w2 = 0.5 # Keep distance away from other hoiks 
        w3 = 0.4 # Match velocity

        ### Rules hoiks follow
        chase = w1 * Rules.chase(self, boids) # Chase the closest boid
        efficiency = w2 * Rules.keep_distance_away(self, hoiks, 50) # Keep distance away from other hoiks. Avoid collision and converging on each other
        align = w3 * Rules.match_velocity(self, boids) # Match velocity 

        # Update size
        self.grow(boids)
        self.shrink()
        self.reproduce(hoiks)
        self.die(hoiks)

        # Update velocity
        self.velocity += chase + efficiency + align

        # Limit the speed of the hoiks 
        if self.size > 10:
            self.velocity.scale_to_length(2)
        else:
            self.velocity.scale_to_length(7)

        # Update position
        self.position += self.velocity

        # Wrap the position of the hoiks
        Rules.bound_position(self)
    






