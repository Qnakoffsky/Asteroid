import pygame
from constants import *
from circleshape import CircleShape
from groups import shots, drawable, updatable

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.bullet_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        points = self.triangle()  # Use your existing triangle calculation method
        pygame.draw.polygon(screen, "white", points)
   
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
        print(f"Before shoot: {self.bullet_timer}")
        if keys[pygame.K_SPACE] and self.bullet_timer <= 0:
            self.shoot()
        print(f"After shoot: {self.bullet_timer}")
        if self.bullet_timer > 0:
            self.bullet_timer -= dt
        if self.bullet_timer < 0:
            self.bullet_timer = 0   

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
    # Start with a unit vector pointing up
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOOT_SPEED

        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        front_position = self.position + forward * self.radius

        shot = Shot(front_position, velocity)
        shots.add(shot)
        self.bullet_timer = PLAYER_SHOOT_COOLDOWN

        return shot

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, position, velocity):
        SHOT_RADIUS = 5
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = velocity

        self.rect = pygame.Rect(0, 0, SHOT_RADIUS*2, SHOT_RADIUS*2)
        self.rect.centerx = int(position.x)
        self.rect.centery = int(position.y)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.centerx = int(self.position.x)
        self.rect.centery = int(self.position.y)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius)
