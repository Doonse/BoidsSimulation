import numpy as np
from pygame import Vector2 as Vector
import random


class Rules:

    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))


    def find_center(self, boids):
            
            # Initialize center vector
            center = Vector(0, 0)
    
            # Loop through all boids
            for boid in boids:
    
                # If the boid is not the boid we are calculating the rule for
                if boid.position != self.position:
    
                    # Add the position of the boid to the center vector
                    center += boid.position
    
            # Return the center vector
            return center / 100


    # Implementing the first rule
    def fly_towards_center(self, boids, center):

        # Initialize perceived center vector
        perceived_center = center

        for boid in boids:

        # If the boid is not the boid we are calculating the rule for   
            if boid.position != self.position: 

                # Add the position of the boid to the center vector
                perceived_center += boid.position 

        # Divide the center vector by the number of boids minus one
        perceived_center = perceived_center / 100 

        # Return the rule multiplied by weight of the rule
        return (perceived_center - self.position) / 100 # 1% movement towards center


    # Implementing second rule, which makes sure boids don't collide with each other
    def keep_distance_away(self, boid):

        # Initialize distance vector
        distance = Vector(0, 0)

        # If the boid is not the boid we are calculating the rule for
        if boid.position != self.position:
            
            # If the distance between the boid and the boid we are calculating the rule for is less than 100
            if self.position.distance_to(boid.position) < 10:

                    # Add the distance vector to the distance vector
                    distance = distance - (self.position - boid.position)

        # Return the distance vector
        return distance
    

    # Implementing the third rule, which adjusts the velocity of the boids to match the velocity of the boids around them
    def match_velocity(self, boid):
    
            # Initialize velocity vector
            velocity = self.velocity

            # If the boid is not the boid we are calculating the rule for
            if boid.position != self.position:
                velocity += boid.velocity

            # Divide the velocity vector by the number of boids minus one
            velocity = velocity / 100

            # Return the rule multiplied by weight of the rule
            return (velocity - self.velocity) / 8


    def tend_to_place(self, boids, hoids):
        # Initialize center vector
        center = Vector(0, 0)

        # Loop through all boids
        for boid in boids:
            for hoid in hoids:

                # If the boid is not the boid we are calculating the rule for
                if boid.position != self.position:
                    
                    if abs(boid.position.x - hoid.position.x) < 50:
                        center.x += 1

                    # Add the position of the boid to the center vector
                    center += boid.position

        # Divide the center vector by the number of boids minus one
        center = center / (len(boids) - 1)

        # Return the rule multiplied by weight of the rule
        return (center - self.position) / 100