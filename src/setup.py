import json, pygame

# Packaging
__all__ = ['config']

# Load the parameters
config = json.load(open('src/parameters.json'))

# Set up pygame
pygame.init()
