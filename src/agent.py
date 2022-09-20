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

        self.p_radius = 200
        self.s_radius = 400

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

        # Repulse - agents too close spread out

        repulse = Vector2D(0, 0)
        for agent in too_close:
            v = self.centre - agent.centre
            repulse = repulse + v.unit

        # Align - agents try and align their direction towards other nearby agents

        align = Vector2D(0, 0)
        if len(close) < 1:
            chance = random.randint(0, 10)
            angle = random.randint(-40, 40)
            align = align if chance != 0 else Vector2D.rotate_vector(self.rotation.unit, angle)
        else:
            for agent in close:
                align = align + agent.rotation

        # Cohesion - agents attempt to steer towards the centre of the group

        cohesion = Vector2D(0, 0)
        if len(close) > 0:
            centres = [agent.centre for agent in close]
            avg_point = Point2D.get_average_point(*centres)
            cohesion = avg_point - self.centre

        # Wall Repulsion - agents steer away from any nearby walls

        walls = self.calculate_wall_repulsion(self)

        forces = (repulse.unit + align.unit + cohesion.unit).unit
        self.rotation = (self.rotation * 0.95 + forces * 0.05).unit
        if walls.magnitude != 0:
            self.rotation = (self.rotation * 0.95 + walls * 0.05).unit

        self.centre = self.centre + self.rotation * 4

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

    @staticmethod
    def calculate_wall_repulsion(agent):
        x, y = agent.x, agent.y
        ex, ey = config['ENVSIZE'][0], config['ENVSIZE'][1]
        ec = Point2D(ex / 2, ey / 2)
        rx, ry = config['XREPULSION'], config['YREPULSION']

        if x < ex * rx:
            return (ec - agent.centre).unit / (abs(x) / (ex * rx))**2
        elif x > ex - (ex * rx):
            return (ec - agent.centre).unit / (abs(ex - x) / (ex * rx))**2
        elif y < ey * ry:
            return (ec - agent.centre).unit / (abs(y) / (ey * ry))**2
        elif y > ey - (ey * ry):
            return (ec - agent.centre).unit / (abs(ey - y) / (ey * ry))**2
        else:
            return Vector2D(0, 0)
