import numpy as np
import pygame as pg


class Boid:
    
    def __init__(self, position, velocity, acceleration, max_speed, max_force):
        self.position = np.array(position, dtype=np.float64)
        self.velocity = np.array(velocity, dtype=np.float64)
        self.acceleration = np.array(acceleration, dtype=np.float64) 
        self.max_speed = max_speed
        self.max_force = max_force

    
    def update(self, boids, alignment_weight, cohesion_weight, separation_weight, obstacle_weight, obstacles):
        pass

    def flockmates(self, boids, distance):
        return [boid for boid in boids if np.linalg.norm(boid.position - self.position) < distance and boid != self]
    


    # Rules class ---
    def alignment_rule(self, flockmates, weight):
        pass

    def cohesion_rule(self, flockmates, weight):
        pass

    def separation_rule(self, flockmates, weight):
        pass

    def obstacle_rule(self, obstacles, weight):
        pass
    # Rules class ---

    def apply_limits(self):
        self.velocity = self.velocity.limit(self.max_speed)
        self.acceleration = self.acceleration.limit(self.max_force)
        self.position = self.position.wrap()
