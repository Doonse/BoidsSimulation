

class Rules:
    # Rules for the boids to follow
    def __init__(self, flock):
        self.boids = flock # Flock of boids 


    def cohesion(self, boid):
        # Boids move towards the center of mass of neighboring boid
        # Find the center of mass of the flock
        # Move towards the center of mass
        pass

    def separation(self, boid):
        # Boids avoid crowding local flockmates
        # Find the distance between the boid and its neighbors
        # If the distance is less than a certain threshold, move away from the neighbor
        pass

    def alignment(self, boid):
        # Boids try to match velocity with near boids
        # Find the average velocity of the flock
        # Move towards the average velocity
        pass

    def avoidance(self, boid):
        # Boids avoid hitting walls
        # Find the distance between the boid and the walls
        # If the distance is less than a certain threshold, move away from the wall
        pass

    def update(self):
        # Update the boids
        pass





    


    


