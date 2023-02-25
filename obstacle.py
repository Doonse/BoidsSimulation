# Pygame
import pygame
from pygame import Vector2

# Random
import random


class Obstacle:
    def __init__(self, screen_width, screen_height, margin=100):
        self.position = Vector2(random.randrange(margin, screen_width - margin), random.randrange(margin, screen_height - margin))
        self.radius = 10
        self.size = self.radius

    def draw(self, screen):
        pygame.draw.ellipse(screen, (0, 100, 200), (self.position.x - self.radius, self.position.y - self.radius, self.radius * 2, self.radius * 2), self.radius)
