import numpy as np
from pygame import Vector2 as Vector
import random

class Rules:
    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))

    # Implementing the first rule: (b_1.position + b_2.position + ... + b_{J-1}.position + b_{J+1}.position + ... + b_N.position) / (N-1)
    def fly_towards_center(self, boid):

        # Weight of the rule
        weight = 0.5
        
        # Initialize center vector
        center = Vector(0, 0) 
    
        # If the boid is not the boid we are calculating the rule for   
        if boid.position != self.position: 

            # Add the position of the boid to the center vector
            center += boid.position 

        # Divide the center vector by the number of boids minus one
        center = center / (99) 

        # Return the rule multiplied by weight of the rule
        return weight * (center - self.position) / 100 


    # Implementing second rule, which makes sure boids don't collide with each other
    def keep_distance_away(self, boid):

        # Weight of the rule
        weight = 0.3

        # Initialize distance vector
        distance = Vector(0, 0)

        # If the boid is not the boid we are calculating the rule for
        if boid.position != self.position:
            
            # If the distance between the boid and the boid we are calculating the rule for is less than 100
            if self.position.distance_to(boid.position) < 10:
                    
                    # Add the distance vector to the distance vector
                    distance += weight * (self.position - boid.position)

        # Return the distance vector
        return distance
    

    # Implementing the third rule, which adjusts the velocity of the boids to match the velocity of the boids around them
    def match_velocity(self, boid):
            
            # Weight of the rule
            weight = 0.4
    
            # Initialize velocity vector
            velocity = self.velocity

            # If the boid is not the boid we are calculating the rule for
            if boid.position != self.position:
                velocity += boid.velocity

            # Divide the velocity vector by the number of boids minus one
            velocity = velocity / (99)

            # Return the rule multiplied by weight of the rule
            return weight * (velocity - self.velocity) / 8