import pygame as pg
from boid import Boid
from flock import Flock

SCREEN_WIDTH = 800 # Width of the screen
SCREEN_HEIGHT = 600 # Height of the screen 
NUM_BOIDS = 50 # Number of boids in the simulation 
BOID_RADIUS = 5 # Radius of the boids
BOID_SPEED = 3 # Speed of the boids
BOID_ACCELERATION = 0.1 # Acceleration of the boids
ALIGNMENT_WEIGHT = 1.0 # Weight of the alignment rule
COHESION_WEIGHT = 1.0 # Weight of the cohesion rule
SEPARATION_WEIGHT = 1.5 # Weight of the separation rule
AVOIDANCE_WEIGHT = 2.0 # Weight of the avoidance rule

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