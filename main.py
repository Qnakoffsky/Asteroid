import pygame
from constants import *
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from groups import updatable, drawable, asteroids, shots

Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, position):
        SHOT_RADIUS = 5
        velocity = pygame.Vector2(0, 0)
        super().__init__(position, SHOT_RADIUS, velocity)
        self.velocity = velocity
        pygame.sprite.Sprite.__init__(self)

def main():
    pygame.init()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    print("Starting Asteroids!")
    
    while True:
        # At the beginning of your main game loop
        print(f"Number of asteroids: {len(asteroids)}")
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        # Update game objects
        updatable.update(dt)
        
        # Check for collisions
        for asteroid in asteroids:
            if player.collision_event(asteroid):
                print("Game over!")
                import sys
                sys.exit()
        
        # Fill screen and draw objects
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
            
        # Update display and timing
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
