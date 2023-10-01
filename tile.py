import pygame
from settings import * 

class Tile(pygame.sprite.Sprite): #! very important to inherit from pygame.sprite.Sprite
    #sprite type will help control our different tiles later on, surface being set by tilesize
    def __init__(self, position, groups, sprite_type, surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups) # initialize the sprite groups
        self.sprite_type = sprite_type # set the sprite type for enemies/objects/details in future update
        self.image = surface # set the image to the surface
        if sprite_type == 'object':
            # do an offset if an object is being created due to size issues
            self.rect = self.image.get_rect(topleft = (position[0], position[1] - TILESIZE)) # if we are placing a large object then we need to offset the position by the tilesize to prevent overlap
        else:
            self.rect = self.image.get_rect(topleft=position) # set the rect to the position of the tile
        self.hitbox = self.rect.inflate(0, -10) # inflate the hitbox to the size of the tile