import pygame as pg
import random 
import numpy as np
from boid_test import Boid # Import the Boid class from boid_test.py, its testing
from hoid import Hoid

WIDTH = 1200
HEIGHT = 900

def main(WIDTH, HEIGHT):
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill("BLACK")
    pg.display.set_caption("Boids")
    clock = pg.time.Clock()

    boids = [Boid(random.randrange(500, 600), random.randrange(500, 600)) for i in range(100)]
    hoids = [Hoid(random.randrange(500, 600), random.randrange(500, 600)) for i in range(2)]


    running = True
    while running:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((0, 0, 0))

        # Boid loop
        for boid in boids: 

            
            boid.draw(screen)
            boid.update(boids)
            
        # Hoid loop         
        for hoid in hoids:
            hoid.draw(screen)
            hoid.update(hoid.bound_position(hoids))



        # Update the screen
        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main(WIDTH, HEIGHT)
