from circleshape import CircleShape
import pygame
import random
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

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_vector_1 = self.velocity.rotate(random_angle)
            new_vector_2 = self.velocity.rotate(-random_angle)
            halfbaked_asteroid_1 = Asteroid(self.rect.centerx, self.rect.centery, new_radius)
            halfbaked_asteroid_2 = Asteroid(self.rect.centerx, self.rect.centery, new_radius)
            halfbaked_asteroid_1.velocity = new_vector_1 * 1.2 
            halfbaked_asteroid_2.velocity = new_vector_2 * 1.2
