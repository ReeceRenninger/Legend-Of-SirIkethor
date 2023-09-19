import pygame
from settings import * 

class Tile(pygame.sprite.Sprite): #! very important to inherit from pygame.sprite.Sprite
    def __init__(self, position, groups):
        super().__init__(groups) # initialize the sprite groups
        self.image = pygame.image.load('graphics/rock.png').convert_alpha() # load the image
        
        self.rect = self.image.get_rect(topleft=position)
        self.hitbox = self.rect.inflate(0, -10) # inflate the hitbox to the size of the tile