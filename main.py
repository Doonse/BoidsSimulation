import pygame as pg
<<<<<<< HEAD
import random 
import numpy as np
from boid import Boid # Import the Boid class from boid_test.py, its testing
from hoid import Hoid
=======

from boid import Boid
from hoik import Hoik
from obstacle import Obstacle


>>>>>>> b1a01d62027e570bffe284fe39d96d76d2c67ead

WIDTH = 1200
HEIGHT = 900

def main(WIDTH, HEIGHT):
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill("BLACK")
    pg.display.set_caption("Boids")
    clock = pg.time.Clock()

    # Create boids, hoiks and obstacles
    boids = [Boid(WIDTH, HEIGHT) for i in range(100)]
    hoiks = [Hoik(WIDTH, HEIGHT) for i in range(2)]
    obstacles = [Obstacle(WIDTH, HEIGHT) for i in range(3)]

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((0, 0, 0))

        # Boid loop 
        for boid in boids: 
            boid.draw(screen)
            boid.update(boids, hoiks, obstacles)

        # Hoik loop         
        for hoik in hoiks:
            hoik.draw(screen)
            hoik.update(boids, hoiks)

        # Obstacle loop
        for obstacle in obstacles:
            obstacle.draw(screen)

        

        # Update the screen
        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main(WIDTH, HEIGHT)
