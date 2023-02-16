import numpy as np
from pygame import Vector2 as Vector
import random

class Rules:
    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)
        self.velocity = Vector(random.uniform(-1, 1), random.uniform(-1, 1))
        self.width = width
        self.height = height
    
    def cohesion(self, boids):
        turn = Vector(*np.zeros(2))
        m = 0
        center_of_mass = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < 50:
                center_of_mass += boid.position
                m += 1
        if m > 0:
            center_of_mass /= m
            center_of_mass = Vector(*center_of_mass)
            vec_to_com = center_of_mass - self.position
            if np.linalg.norm(vec_to_com) > 0:
                vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * self.max_speed
            turn = vec_to_com - self.velocity
            if np.linalg.norm(turn)> self.max_force:
                turn = (turn /np.linalg.norm(turn)) * self.max_force

        return turn

    def separation(self, boids):
        turn = Vector(*np.zeros(2))
        m = 0
        average = Vector(*np.zeros(2))
        for boid in boids:
            distance = np.linalg.norm(boid.position - self.position)
            if self.position != boid.position and distance < 50:
                diff = self.position - boid.position
                diff /= distance
                average += diff
                m += 1
        if m > 0:
            average /= m
            average = Vector(*average)
            if np.linalg.norm(turn) > 0:
                avg_vector = (average / np.linalg.norm(turn)) * self.max_speed
            turn = average - self.velocity
            if np.linalg.norm(turn)> self.max_force:
                steering = (turn /np.linalg.norm(turn)) * self.max_force

        return turn

    def alignment(self, boids):
        turn = Vector(*np.zeros(2))
        m = 0
        average = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < 50:
                average += boid.velocity
                m += 1
        if m > 0:
            average /= m
            average = Vector(*average)
            average = (average /np.linalg.norm(average)) * self.max_speed
            turn = average - self.velocity

        return turn

