
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, initial_velocity):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(initial_velocity)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # calculate random angle
        random_angle = random.uniform(20, 50)
        # calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # create two new velocity vectors by rotating the current velocity
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
        
        # create new asteroids
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity1)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, new_velocity2)
        
        # add them to the same groups as the original asteroid
        for group in self.groups():
            group.add(new_asteroid1)
            group.add(new_asteroid2)

    def update(self, dt):
        self.position += self.velocity * dt