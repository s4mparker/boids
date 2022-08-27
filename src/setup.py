import pygame

from . import Window

# Parameters
WIDTH        = 400
HEIGHT       = 400
BACKGROUND   = 0, 0, 0

# PyGame
pygame.init()

# Simulation
w = Window(scene=None, size=(WIDTH, HEIGHT), background=BACKGROUND)
