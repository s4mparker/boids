import pygame, sys

from . import SIZE, BACKGROUND

# Packaging
__all__ = ['Window']

class Window:

    def __init__(self, scene, **kwargs):
        self.screen = pygame.display.set_mode(size=(SIZE, SIZE))
        # insert call to scene
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    self.screen.fill(BACKGROUND)
                    pygame.display.flip()
