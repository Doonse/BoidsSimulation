import pygame as pg
import random 
import numpy as np
from boid import Boid

WIDTH = 800
HEIGHT = 600


def main(WIDTH, HEIGHT):
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill("BLACK")
    pg.display.set_caption("Boids")
    clock = pg.time.Clock()
    boids = [Boid(random.randrange(100, 800), random.randrange(100, 800), 1, 1) for i in range(20)]
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for boid in boids:
            boid.update(boids)
            boid.draw(screen)
            boid.edge_wrap(WIDTH, HEIGHT)
        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main(WIDTH, HEIGHT)
