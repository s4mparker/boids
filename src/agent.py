import pygame, random, math, functools

from . import Point2D, Vector2D, config

# Packaging
__all__ = ['Agent']

class Agent(pygame.sprite.Sprite):

    def __init__(self, x, y, size, speed=1):
        super().__init__()

        self.centre   = Point2D(x, y)
        self.rotation = Vector2D(0, 1)
        self.speed    = speed

        self.p_radius = 100
        self.s_radius = 1000

        self.sprite = pygame.Surface(size=(size, size))
        self.sprite.fill(config['BLACK'])
        self.sprite.set_colorkey(config['BLACK'])
        pygame.draw.polygon(self.sprite, config['WHITE'], points=[(0, size), (size, size), (int(size * 0.5), 0)])

    def update(self):
        group = set(self.groups()[0].sprites()) - {self}

        too_close, close = set(), set()
        for agent in group:
            distance = self.get_distance_between_agents(self, agent)
            if distance <= self.p_radius:
                too_close.add(agent)
            elif distance <= self.s_radius:
                close.add(agent)

        repulse = Vector2D(0, 0)
        for agent in too_close:
            v = self.centre - agent.centre
            repulse = repulse + (v.unit * 0.5)

        align = Vector2D(0, 0)
        if len(close) < 1:
            chance = random.randint(0, 10)
            angle = random.randint(-40, 40)
            align = align if chance != 0 else Vector2D.rotate_vector(self.rotation.unit, angle)
        else:
            sum = Vector2D(0, 0)
            for agent in close:
                sum = sum + agent.rotation

            print(type(sum))
            print(type(self.rotation))
            # align = 0.5 * sum.unit # + (0.5 * self.rotation.unit)
            align = sum + self.rotation

        centre = Vector2D(0, 0)
        if len(close) > 0:
            avg_point = Point2D.get_average_point(*list(close))
            centre = 0.5 * (avg_point - self.centre)

        self.rotation = (self.rotation * 0.5 + repulse.unit + align.unit + centre.unit).unit
        self.centre = self.centre + self.rotation * 10




        

        

        # if random.randint(0, 10) == 0:
        #     angle = random.randint(-10, 10)
        #     self.rotation = Vector2D.rotate_vector(self.rotation, angle)
        # self.centre   = self.centre + self.rotation.unit

        # # self.rotation = Vector2D.rotate_vector(self.rotation, 100)

    @property
    def x(self):
        return self.centre.x

    @property
    def y(self):
        return self.centre.y

    @property
    def image(self):
        return pygame.transform.rotate(self.sprite, self.rotation.angle + 180)

    @property
    def rect(self):
        c = (int(self.sprite.get_width() / 2), int(self.sprite.get_height() / 2))
        o_rect = self.sprite.get_rect(center = c)
        r_rect = self.image.get_rect(center = o_rect.center)
        r_rect.center = (self.centre.x, self.centre.y)
        return r_rect

    @staticmethod
    def get_distance_between_agents(agent1, agent2):
        return math.sqrt((agent1.x - agent2.x)**2 + (agent1.y - agent2.y)**2)
