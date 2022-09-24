import pygame, sys, random

from . import Agent, config

# Packaging
__all__ = ['Simulation']

class Simulation:

    @staticmethod
    def Run():
        screen_dims      = (config['SCREEN']['X'], config['SCREEN']['Y'])
        environment_dims = (config['ENVIRONMENT']['X'], config['ENVIRONMENT']['Y'])

        screen = pygame.display.set_mode(size=screen_dims)
        environment = pygame.Surface(size=environment_dims)

        all_agents = pygame.sprite.Group()
        for type in [type for type in config['AGENTS'].keys()]:
            quantity = config['AGENTS'][type]['QUANTITY']
            for i in range(quantity):
                agent    = Agent(agent_type=type)
                all_agents.add(agent)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            environment.fill(config['COLOURS']['BLACK'])

            all_agents.update()
            all_agents.draw(environment)

            scaled_environment = pygame.transform.smoothscale(environment, size=screen_dims)

            screen.fill(config['COLOURS']['BLACK'])
            screen.blit(scaled_environment, scaled_environment.get_rect())
            pygame.display.flip()
            pygame.event.wait(10)

