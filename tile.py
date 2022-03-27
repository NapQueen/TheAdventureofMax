import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def _init_(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../start setup/graphics/test/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
