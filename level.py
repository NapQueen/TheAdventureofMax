import pygame
from settings import *
from tile import Tile
from cat import Cat

class Level:
    def __inti__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                # print(row_index)
                # print(row)
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.ostacles_sprites])
                if col == 'c':
                    Cat((x,y),[self.visible_sprites])

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)