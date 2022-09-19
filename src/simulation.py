import pygame, sys, random

from . import Agent, config

# Packaging
__all__ = ['Simulation']

class Simulation:

    @staticmethod
    def Run():
        screen = pygame.display.set_mode(size=config['SCREENSIZE'])
        environment = pygame.Surface(size=config['ENVSIZE'])

        agents = pygame.sprite.Group()
        for i in range(10):
            agents.add(Agent(
                x = random.randint(0, config['ENVSIZE'][0]),
                y = random.randint(0, config['ENVSIZE'][1]),
                size = 100
            ))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            environment.fill(config['BLACK'])
            agents.update()
            agents.draw(environment)

            scaled_environment = pygame.transform.smoothscale(environment, size=config['SCREENSIZE'])

            screen.fill(config['BLACK'])
            screen.blit(scaled_environment, scaled_environment.get_rect())
            pygame.display.flip()
            pygame.event.wait(2)

