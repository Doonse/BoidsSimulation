import pygame as pg
import random 
import numpy as np
from boid import Boid
from hoid import Hoid

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
    boids = [Boid(random.randrange(500, 600), random.randrange(500, 600)) for i in range(100)] 
    # Initialize hoids with random positions
    hoids = [Hoid(random.randrange(500, 600), random.randrange(500, 600)) for i in range(2)]

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
            # The rules control the movement of the boids 
            boid.update(boids)

            # Bound the boids to the screen so they don't fly off
            boid.wrap_position(boids)
        
        for hoid in hoids:
            hoid.draw(screen)
            hoid.update(hoid.bound_position(hoids))

        # Update the screen
        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main(WIDTH, HEIGHT)
