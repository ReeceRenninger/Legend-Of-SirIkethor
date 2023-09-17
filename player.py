import pygame
from settings import * 

class Player(pygame.sprite.Sprite): #! very important to inherit from pygame.sprite.Sprite
    def __init__(self, position, groups, obstacle_sprites):
        super().__init__(groups) # initialize the sprite groups
        self.image = pygame.image.load('graphics/knight.png').convert_alpha() # load the image
        
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2(0, 0) # create a vector for the direction of the player, this is what we can influence with keystrokes to move the player
        self.speed = 5 # set the speed of the player to 5

        self.obstacle_sprites = obstacle_sprites

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

    def move(self, speed):
        if self.direction.magnitude() != 0: # vector was set to 0 if no key was pressed, so if the magnitude is not 0, normalize the vector
            self.direction = self.direction.normalize() # normalize the vector by dividing the vector by the magnitude, this helps keep movement fluid if 2 keys are pressed at the same time
            self.rect.x += self.direction.x * speed # move the player rect by the direction * the speed
            self.collision("horizontal") # check for horizontal collision
            self.rect.y += self.direction.y * speed # move the player rect by the direction * the speed
            self.collision("vertical") # check for vertical collision

        # self.rect.center += self.direction * speed # move the player rect by the direction * the speed

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left # set the right side of the player rect to the left side of the obstacle rect
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right # set the left side of the player rect to the right side of the obstacle rect
        
        if direction == "vertical":
                for sprite in self.obstacle_sprites:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0: # moving down
                            self.rect.bottom = sprite.rect.top # set the bottom side of the player rect to the top side of the obstacle rect
                        if self.direction.y < 0: # moving up
                            self.rect.top = sprite.rect.bottom # set the top side of the player rect to the bottom side of the obstacle rect
    def update(self):
        self.input()
        self.move(self.speed) # move the player by the speed