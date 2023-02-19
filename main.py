import pygame as pg
import random
from boid import Boid # Import the Boid class from boid_test.py, its testing
from hoik import Hoid

WIDTH = 1200
HEIGHT = 900

def main(WIDTH, HEIGHT):
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    screen.fill("BLACK")
    pg.display.set_caption("Boids")
    clock = pg.time.Clock()

    boids = [Boid(random.randrange(0, WIDTH), random.randrange(0, HEIGHT)) for i in range(100)]
    hoiks = [Hoid(random.randrange(0, WIDTH), random.randrange(0, HEIGHT)) for i in range(2)]


    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill((0, 0, 0))

        # Boid loop 
        for boid in boids: 
            boid.draw(screen)
            boid.update(boids, WIDTH, HEIGHT)

            
        """ # Hoid loop         
        for hoik in hoiks:
            hoik.draw(screen)
            hoik.update(boids) """


        # Update the screen
        pg.display.flip()
        clock.tick(60)
    pg.quit()

if __name__ == "__main__":
    main(WIDTH, HEIGHT)
