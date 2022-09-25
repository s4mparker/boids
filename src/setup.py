import pygame

from json import load

# Packaging
__all__ = ['config']

# Load the parameters
config = load(open('parameters.json'))

# Set up pygame
pygame.init()
pygame.display.set_caption('Boids Simulation')
