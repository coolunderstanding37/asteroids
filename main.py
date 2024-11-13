import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 74)
pygame.display.set_caption('Asteroids')

print(f"Starting asteroids!")
print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

clock = pygame.time.Clock()
dt = clock.tick(60) / 1000

# Create groups
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
shots = pygame.sprite.Group()

# set containers in the Asteroid class definition
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

# Example values before creating an asteroid instance
x = 100  # Initial x-coordinate
y = 150  # Initial y-coordinate
radius = 30  # Radius of the asteroid
initial_velocity = pygame.Vector2(1, 1)  # Starting velocity vector

# instantiate the player
player = Player(
    SCREEN_WIDTH / 2,
    SCREEN_HEIGHT / 2,
    shots,
    updatable,
    drawable
    )

#instantiate the asteroid instances
asteroid = Asteroid(x, y, radius, initial_velocity)
asteroid.velocity = initial_velocity

# add player to both groups
updatable.add(player)
drawable.add(player)

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

    if not paused:
        # Update game logic only if not paused
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Update all updatables
        for sprite in updatable:
            sprite.update(dt)  # Ensure 'dt' is your delta time for smooth movement

        # iterate through asteroids
        for rock in asteroids:
            if rock.collision(player):
                print("GAME OVER!")
                sys.exit()

        # Call the draw methods of drawable sprites
        for sprite in drawable:
            sprite.draw(screen)
        
        # Refresh the display
        pygame.display.flip()
        
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

        # Calculate position to center text within each button
        resume_text_x = resume_button.x + (resume_button.width - resume_text.get_width()) // 2
        resume_text_y = resume_button.y + (resume_button.height - resume_text.get_height()) // 2
        screen.blit(resume_text, (resume_text_x, resume_text_y))

        quit_text_x = quit_button.x + (quit_button.width - quit_text.get_width()) // 2
        quit_text_y = quit_button.y + (quit_button.height - quit_text.get_height()) // 2
        screen.blit(quit_text, (quit_text_x, quit_text_y))
        
        # update screen
        pygame.display.flip()
