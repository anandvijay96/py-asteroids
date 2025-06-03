# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game over!")
                running = False
            for shot in shots:
                if asteroid.checkCollision(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for asteroid in drawable:
            asteroid.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()
if __name__ == "__main__":
    main()
