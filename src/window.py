import pygame, sys

# Packaging
__all__ = ['Window']

class Window:

    def __init__(self, scene, size, background):
        self.size       = size
        self.background = background

        self.screen = pygame.display.set_mode(size=self.size)
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.screen.fill(self.background)
            pygame.display.flip()

