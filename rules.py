
from pygame import Vector2 as Vector

class Rules:
    def __init__(self, boids):
        self.boids = boids
        self.cohesion = 0.01
        self.separation = 0.1
        self.alignment = 0.1

    def cohesion(self, boids): # boids is a list of boids
        center = Vector(0, 0) # center is a vector
        for boid in boids: # boid in boids
            center += boid.position # add the position of the boid to the center vector
        center /= len(boids) # divide the center vector by the number of boids
        return 0.3 * (center - self.position) / 1000 # return the vector from the center of the boids to the boid

    def separation(self, boids):
        distance = Vector(0, 0)
        for boid in boids:
            if boid.position != self.position:
                if (boid.position - self.position).length() < 5:
                    distance += 0.1 * (self.position - boid.position) 
        return distance

    def alignment(self, boids):
        velocity = Vector(0, 0) 
        for boid in boids:
            velocity += boid.velocity
        velocity /= len(boids)
        return  0.3 * (velocity - self.velocity) / 8
    

