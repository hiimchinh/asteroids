import pygame
import random

from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        ast_1_velocity = self.velocity.rotate(angle)
        ast_2_velocity = self.velocity.rotate(-angle)
        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_1.velocity = ast_1_velocity * 1.2
        ast_2.velocity = ast_2_velocity * 1.2
