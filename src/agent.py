import pygame, random, math

from . import Point2D, Vector2D, BLACK, WHITE, RED, SIZE, calculate_repulsion

# Packaging
__all__ = ['Agent']

class Agent(pygame.sprite.Sprite):

    def __init__(self, environment):
        super().__init__()

        self.environment = environment
        self.neighbours  = []

        (w, h) = self.environment.get_size()
        self.position    = Point2D.random(w, h)
        self.bearing     = Vector2D.random(w, h).unit / 100
        self.radius      = 8

        self.circle      = self.create_image(self.radius)

    def __str__(self):
        return f'Agent: {len(self.neighbours)}'

    def update(self):
        repulsion = calculate_repulsion(self.position)
        if repulsion is not None:
            self.bearing = repulsion
        else:
            a = random.randint(-10, 10) * math.pi / 1800
            self.bearing = Vector2D(
                math.cos(a) * self.bearing.x - math.sin(a) * self.bearing.y,
                math.sin(a) * self.bearing.x + math.cos(a) * self.bearing.y
            )

        self.position = (self.position + self.bearing.unit * 0.02)

    def draw(self):
        image = pygame.transform.rotate(self.circle, self.bearing.bearing)
        rect = image.get_rect()
        rect.centerx = self.position.x
        rect.centery = self.position.y
        self.environment.blit(image, rect)

    def addNeighbours(self, *neighbours):
        self.neighbours.extend(neighbours)

    def inCollision(self, agent):
        if type(agent) is not Agent:
            raise TypeError('expected an Agent')
        dx = self.x - agent.x
        dy = self.y - agent.y
        dz = math.sqrt(dx**2 + dy**2)
        return dz <= (self.radius + agent.radius)

    @staticmethod
    def create_image(r):
        image = pygame.Surface(size=(r*2, r*2))
        image.set_colorkey(BLACK)
        image.fill(BLACK)
        pygame.draw.circle(image, color=WHITE, center=(r, r), radius=r)
        pygame.draw.line(image, color=RED, start_pos=(r, r), end_pos=(r, 0), width=int(r/4))
        return image

    