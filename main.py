import pygame as pg
from boid import Boid
from flock import Flock

def main():
    # initialize pygame and screen with borders
    pg.init()
    screen = pg.display.set_mode((800, 600))
    pg.display.set_caption("Boids")
    clock = pg.time.Clock()
    running = True

    # create a flock of boids
    flock = Flock(400, 300)
    for i in range(10):
        flock.addBoid(Boid(400, 300))

    # main loop
    while running:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # update and draw
        screen.fill((0, 0, 0))
        flock.update()
        flock.draw(screen)
        pg.display.flip()

if __name__ == "__main__":
    main()