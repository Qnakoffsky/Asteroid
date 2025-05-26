import pygame
import sys
from constants import *
from player import Player, Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from groups import updatable, drawable, asteroids, shots

def main():
    pygame.init()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
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
                sys.exit()
            for asteroid in asteroids:
                for bullet in shots:
                    if bullet.collision_event(asteroid):
            # They collided! Destroy both
                        asteroid.split()
                        bullet.kill()

 # Fill screen and draw objects
        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        # Update display and timing
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
