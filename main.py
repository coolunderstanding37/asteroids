import pygame
import sys
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Asteroids')

clock = pygame.time.Clock()
dt = clock.tick(60) / 1000

font = pygame.font.Font(None, 74)

print(f"Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Toggle paused state
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            paused = not paused

        if paused and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            # handle Resume button click
            if resume_button.collidepoint(mouse_pos):
                paused = False

            if quit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

        # Handle active event to toggle paused state
        if event.type == pygame.ACTIVEEVENT:
            if event.gain == 0:    # window not active - pause game
                paused = True
            if event.gain == 1:    # window is active - game not paused
                paused = False

    if not paused:
        # Update game logic only if not paused
        pygame.display.flip()
        screen.fill((0, 0, 0))
        dt = clock.tick(60) / 1000
    else:
        # render paused screen
        paused_text = font.render('Paused', True, (255, 255, 255))
        screen.blit(paused_text, (SCREEN_WIDTH//2 - paused_text.get_width()//2, 50))

        # Draw buttons
        resume_button = pygame.Rect((SCREEN_WIDTH//2 - 100, 150, 200, 50))
        quit_button = pygame.Rect((SCREEN_WIDTH//2 - 100, 250, 200, 50))

        pygame.draw.rect(screen, (0, 255, 0), resume_button)
        pygame.draw.rect(screen, (255, 0, 0), quit_button)

        # Add button text
        resume_text = font.render('Resume', True, (0, 0, 0))
        quit_text = font.render('Quit', True, (0, 0, 0))
        screen.blit(resume_text, (resume_button.x + 50, resume_button.y + 8))
        screen.blit(quit_text, (quit_button.x + 60, quit_button.y + 8))

