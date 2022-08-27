import pygame, random

class Entity(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.color     = 1, 1, 1
        self.direction = random.randint(0, 359)