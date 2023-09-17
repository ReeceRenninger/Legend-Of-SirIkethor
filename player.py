import pygame
from settings import * 

class Player(pygame.sprite.Sprite): #! very important to inherit from pygame.sprite.Sprite
    def __init__(self, position, groups):
        super().__init__(groups) # initialize the sprite groups
        self.image = pygame.image.load('graphics/knight.png').convert_alpha() # load the image
        
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2(0, 0) # create a vector for the direction of the player, this is what we can influence with keystrokes to move the player
    def input(self):
        keys = pygame.key.get_pressed() # get the keys that are pressed

        if keys[pygame.K_UP]:
            self.direction.y = -1 # set the y direction to -1 to move up
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1 # set the y direction to 1 to move down
        else:
            self.direction.y = 0 # set the y direction to 0 if no key is pressed

         
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1 # set the x direction to 1 to move right
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1 # set the x direction to -1 to move left
        else:
            self.direction.x = 0 # set the x direction to 0 to not move if no key is pressed
    def update(self):
        self.input()