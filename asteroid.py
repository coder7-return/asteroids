import pygame
import random # New: Import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event # New: Import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white", 
            self.position, 
            self.radius, 
            LINE_WIDTH
        )
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # 1. Always kill itself
        self.kill()

        # 2. If it's a small asteroid, we are done
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # 3. Otherwise, spawn 2 smaller asteroids
        log_event("asteroid_split")
        
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generate random angle for divergence
        angle = random.uniform(20, 50)
        
        # Calculate new velocities
        # Original velocity rotated by +angle
        velocity_1 = self.velocity.rotate(angle) * 1.2
        # Original velocity rotated by -angle (opposite direction)
        velocity_2 = self.velocity.rotate(-angle) * 1.2
        
        # Create two new Asteroids
        # They are created at the current position, and automatically added to their groups
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = velocity_1
        
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = velocity_2