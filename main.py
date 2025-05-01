import pygame
from constants import *
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from circleshape import CircleShape
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
   pygame.init()
   Player.containers = (updatable, drawable)
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   clock = pygame.time.Clock()
   dt = 0
   print("Starting Asteroids!") #deleting print statements
   while True:
     screen.fill("black")  #fills with black surface
     for object in drawable:
         object.draw(screen)
     pygame.display.flip() #updates screen
     dt = clock.tick(60) / 1000

     updatable.update(dt)

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             return
if __name__ == "__main__":
    main()
