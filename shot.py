from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y, initial_velocity):
        super().__init__(x, y, SHOT_RADIUS)
        pygame.sprite.Sprite.__init__(self)
        self.velocity = initial_velocity
        
        # placeholder image
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA)
        # placeholder rect
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = (self.position.x, self.position.y)