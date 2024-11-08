# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

print(f"Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Handle active event to toggle paused state
        if event.type == pygame.ACTIVEEVENT:
            if event.gain == 0:    # window not active - pause game
                paused = True
            if event.gain == 1:    # window is active - game not paused
                paused = False

    if not paused:
        # run game update and rendering logic only if not paused
        screen.fill((0, 0, 0))
        pygame.display.flip()

