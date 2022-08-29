import pygame, sys

from . import SIZE, BLACK, Agent

# Packaging
__all__ = ['Simulation']

class Simulation:

    @classmethod
    def Run(cls):
        screen = pygame.display.set_mode(size=(SIZE, SIZE))

        agents = pygame.sprite.Group([Agent() for i in range(5)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            screen.fill(BLACK)
            agents.update()
            agents.draw(screen)
            pygame.display.flip()
            pygame.event.wait(2)

