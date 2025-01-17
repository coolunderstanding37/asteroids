import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from circleshape import *
from shot import Shot

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, shots, updatable, drawable):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0   # initializes rotation attribute
        self.shots = shots
        self.updatable = updatable
        self.drawable = drawable
        self.timer = 0    

        # placeholder image
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        # placeholder rect
        self.rect = self.image.get_rect(center=(x, y))
        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def shoot(self):
        # Create vector pointing up
        shot_direction = pygame.Vector2(0, 1)
        # Rotate it to match player direction
        shot_direction = shot_direction.rotate(self.rotation)
        # Scale it up
        shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
        
        # Create new shot
        new_shot = Shot(self.position.x, self.position.y, shot_velocity)

        self.shots.add(new_shot)
        self.updatable.add(new_shot)
        self.drawable.add(new_shot)

    def rotate(self, dt):
        # update rotation angle
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        # rotating player
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        # moving player
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # shooting cooldown and timer
        self.timer -= dt
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN

        # player wrap around screen
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT