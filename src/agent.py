import pygame
import numpy as np

from functools import reduce

from . import Point2D, Vector2D, config

# Packaging
__all__ = ['Agent']

class Agent(pygame.sprite.Sprite):

    agents = set()

    def __init__(self, agent_type):

        # Call the superclass' constructor
        super().__init__()

        # Set the agent's type
        self.type = agent_type
        attributes = config['AGENTS'][agent_type]

        # Add the agent being created to the wider population of agents
        self.agents.add(self)

        # Generate a random starting point in the environment
        self.centre = Point2D(
            x=np.random.randint(0, config['ENVIRONMENT']['X']),
            y=np.random.randint(0, config['ENVIRONMENT']['Y']),
        )

        # Set the agent's initial direction to (0, 1) aka up
        self.direction = Vector2D(x=0, y=1)

        # Extract the agent's attributes from the configuration file
        self.speed = float(max(0, 
            np.random.normal(
                loc   = attributes['SPEED']['MEAN'],
                scale = attributes['SPEED']['STD']
            )
        ))
        self.turning = float(np.clip(
            np.random.normal(
                loc   = attributes['TURNING']['MEAN'],
                scale = attributes['TURNING']['STD']
            ),
            a_min=0,
            a_max=1
        ))
        self.force_weights = attributes['FORCE_WEIGHTS']
        self.outer_radius = attributes['OUTER_RADIUS']
        self.inner_radius = attributes['INNER_RADIUS']

        # Generate the agent's sprite
        s = attributes['SIZE']
        self.sprite = pygame.Surface(size=(s, s))
        self.sprite.fill(config['COLOURS']['BLACK'])
        self.sprite.set_colorkey(config['COLOURS']['BLACK'])
        pygame.draw.polygon(
            surface=self.sprite,
            color=config['COLOURS'][attributes['COLOUR']],
            points=[(0, s), (s, s), (int(s*0.5), 0)]
        )

    def update(self):
        
        # Generate three sets of agents based on their type and distance from the agent in question
        attract_like, repulse_like, repulse_other = set(), set(), set()
        for agent in self.agents - {self}:
            distance = self.get_distance_between_agents(self, agent)
            if self.type == agent.type and distance <= self.inner_radius:
                repulse_like.add(agent)
            elif self.type == agent.type and distance <= self.outer_radius:
                attract_like.add(agent)
            elif self.type != agent.type and distance <= self.outer_radius:
                repulse_other.add(agent)

        # Calculate the repulsion forces
        repulsion = (   
            self.calculate_repulsion_force(repulse_like).unit * self.force_weights['REPULSE']['LIKE'] + 
            self.calculate_repulsion_force(repulse_other).unit * self.force_weights['REPULSE']['UNLIKE']
        )

        # Calculate the alignment force
        alignment = self.calculate_alignment_force(attract_like).unit * self.force_weights['ALIGN']

        # Calculate the cohesion force
        cohesion = self.calculate_cohesion_force(attract_like).unit * self.force_weights['COHESION']

        # Update the agent based on the calculated forces
        forces = repulsion + alignment + cohesion
        if forces:
            self.direction = (forces.unit * self.turning + self.direction.unit * (1 - self.turning)).unit
        else:
            self.direction = Vector2D.rotate_vector(
                vector=self.direction,
                angle=np.random.choice([0, 1], p=[0.8, 0.2])*np.random.randint(-5, 5)
            )

        # Calculate the agent's wall repulsion force
        wall_force = self.calculate_wall_repulsion_force().unit

        # Update the agent based on the calculated wall force
        if wall_force:
            wall_turn = 1 - (1 - self.turning)**2
            self.direction = (wall_force.unit * wall_turn + self.direction.unit * (1 - wall_turn)).unit

        # Update the agent's position based on its direction
        self.centre = self.centre + self.direction * self.speed

    def calculate_repulsion_force(self, agents):
        force = reduce(
            lambda a,b: a+(self.centre - b.centre),
            agents,
            Vector2D(x=0, y=0)
        )
        return force

    def calculate_alignment_force(self, agents):
        force = reduce(
            lambda a,b: a+b.direction.unit,
            agents,
            Vector2D(x=0, y=0)
        )
        return force

    def calculate_cohesion_force(self, agents):
        force = Vector2D(x=0, y=0)
        if len(agents) > 0:
            centres = [agent.centre for agent in agents]
            avg_point = Point2D.get_average_point(*centres)
            force = avg_point - self.centre
        return force

    def calculate_wall_repulsion_force(self):
        ex, ey = config['ENVIRONMENT']['X'], config['ENVIRONMENT']['Y'] # environment's dimensions
        rx, ry = config['XREPULSION'], config['YREPULSION'] # environment's repulsion
        centre = Point2D(x=int(ex / 2), y=int(ey / 2))

        if self.x < ex * rx or self.x > ex - (ex * rx):
            return centre - self.centre
        elif self.y < ey * ry or self.y > ey - (ey * ry):
            return centre - self.centre
        else:
            return Vector2D(x=0, y=0)

    # ---- Properties -------------------------------------------------------

    @property
    def x(self):
        return self.centre.x

    @property
    def y(self):
        return self.centre.y

    @property
    def image(self):
        return pygame.transform.rotate(self.sprite, self.direction.angle + 180)

    @property
    def rect(self):
        centre = (int(self.sprite.get_width() / 2), int(self.sprite.get_height() / 2))
        original = self.sprite.get_rect(center = centre)
        rotated = self.image.get_rect(center = original.center)
        rotated.center = (self.centre.x, self.centre.y)
        return rotated

    # ---- Static Methods ---------------------------------------------------

    @staticmethod
    def get_distance_between_agents(a, b):
        return np.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
