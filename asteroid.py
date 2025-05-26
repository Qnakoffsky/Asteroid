from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rect = pygame.Rect(0, 0, radius*2, radius*2)
        self.rect.centerx = int(x)
        self.rect.centery = int(y)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.centerx = int(self.position.x)
        self.rect.centery = int(self.position.y)
