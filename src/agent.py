import pygame, random, math, functools

from . import Point2D, Vector2D, BLACK, WHITE, RED, SIZE, calculate_repulsion

# Packaging
__all__ = ['Agent']

class Agent(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.position = Point2D.random(SIZE, SIZE)
        self.bearing  = Vector2D(0, 1)
        self.radius   = 5
        self.show_bearing = False

        self.base_image = pygame.Surface(size=(self.radius * 2, self.radius * 2))
        self.base_image.fill(BLACK)
        self.base_image.set_colorkey(BLACK)
        pygame.draw.circle(self.base_image, WHITE, center=(self.radius, self.radius), radius=self.radius)
        
        if self.show_bearing:
            pygame.draw.line(self.base_image, RED, start_pos=(self.radius, self.radius), end_pos=(self.radius, 0), width=int(self.radius / 3))

    def __str__(self):
        return f'Agent ({self.position.x}, {self.position.y})'

    @property
    def image(self):
        if self.show_bearing:
            return pygame.transform.rotate(self.base_image, self.bearing.angle)
        else: return self.base_image

    @property
    def rect(self):
        r = self.image.get_rect()
        r.center = (self.position.x, self.position.y)
        return r

    def update(self):
        close = set()
        for neighbour in set(self.groups()[0]) - {self}:
            if math.sqrt((self.position.x - neighbour.position.x)**2 + (self.position.y - neighbour.position.y)**2) - self.radius < self.radius * 10:
                close.add(neighbour)

        if len(close) > 0:
            points   = [c.position for c in close]
            bearings = [c.bearing for c in close]

            separation = Point2D.average(*points) - self.position
            alignment  = Vector2D.average(*bearings)
            self.bearing = separation + alignment

        r = calculate_repulsion(self.position)
        if r is not None:
            self.bearing = self.bearing + r

        self.position = self.position + self.bearing.unit * 0.25
