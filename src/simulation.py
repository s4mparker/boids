import pygame, sys

from . import SIZE, BLACK, Agent

# Packaging
__all__ = ['Simulation']

class Simulation:

    @classmethod
    def Run(cls):
        screen = pygame.display.set_mode(size=(SIZE, SIZE))
        agents = {Agent(environment=screen) for i in range(2)}
        print(f'All: {agents}')
        for agent in agents:
            agent.addNeighbours(*(agents - {agent}))
            print(agent)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            screen.fill(BLACK)
            {agent.update() for agent in agents}
            {agent.draw()   for agent in agents}
            pygame.display.flip()

