import pygame
from constants import *
from circleshape import CircleShape
from groups import shots

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        SHOT_RADIUS = 5
        super().__init__(position, SHOT_RADIUS, velocity)
        self.velocity = velocity
        pygame.sprite.Sprite.__init__(self)
     
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
     
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
     
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        print(f"Space pressed: {keys[pygame.K_SPACE]}")
        if keys[pygame.K_SPACE]:
            print("About to shoot!")
            self.shoot()
     
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
     
    def shoot(self):
        print("Shoot method called")
    # Start with a unit vector pointing up
        direction = pygame.Vector2(0, -1)
        direction = direction.rotate(self.rotation)
        velocity = direction * PLAYER_SHOOT_SPEED
        shot = Shot(self.position, velocity)
        shots.add(shot)

        return shot
