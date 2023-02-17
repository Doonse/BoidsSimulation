import pygame as pg
import random 
import numpy as np
from boid import Boid

WIDTH = 800
HEIGHT = 600


def main(WIDTH, HEIGHT):

    # Initialize pygame
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill("BLACK")
    pg.display.set_caption("Boids")
    clock = pg.time.Clock()

    # Initialize boids with random positions as explained in pseudocode http://www.kfish.org/boids/pseudocode.html
    # Random velociies are assigned in the Boid class as well
    # Acceleration vector is initialized to 0
    # Rest is constant in the Boid class except for the width and height, which are given as an argument
    boids = [Boid(random.randrange(100, 800), random.randrange(10, 500)) for i in range(100)] 

    # Main loop
    running = True
    while running:
        
        # Event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((0, 0, 0))

        # Boid loop
        for boid in boids:
            
            # Draw boids on screen 
            boid.draw(screen)
            
            # Update boids position and velocity 
            # This calls the update function in the Boid class, which consists of the three rules
            # The three rules are called from the Rules class
            # The three rules are cohesion, separation and alignment
            boid.update(boids)

            # Bound the boids to the screen so they don't fly off
            boid.bound_position(boids)

        # Update the screen
        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main(WIDTH, HEIGHT)
