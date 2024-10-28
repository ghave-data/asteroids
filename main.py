import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = updatable


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

    game_is_on = True
    while game_is_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if player.check_collision(obj):
                print("Game Over!")
                sys.exit()
        pygame.Surface.fill(screen, color=(0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()