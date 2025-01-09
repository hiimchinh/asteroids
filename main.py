# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()


    Player.containers = (updatable, drawable)


    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    clock = pygame.time.Clock()
    # delta time
    dt = 0
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # shot
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for i in updatable:
            i.update(dt)
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print('Game over!')
                sys.exit()
        screen.fill(color="Black")
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
