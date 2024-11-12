
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, initial_velocity):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(initial_velocity)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt