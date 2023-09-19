import pygame
from settings import * 

class Player(pygame.sprite.Sprite): #! very important to inherit from pygame.sprite.Sprite
    def __init__(self, position, groups, obstacle_sprites):
        super().__init__(groups) # initialize the sprite groups
        self.image = pygame.image.load('graphics/ikeKnight.png').convert_alpha() # load the image

        self.rect = self.image.get_rect(topleft = position)

        self.hitbox = self.rect.inflate(-15, -30) # changing the rect of player to give depth when traversing obstacles #! may need to change x to 0 for collision issue later on

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
            self.hitbox.x += self.direction.x * speed # move the player hitbox by the direction * the speed
            self.collision("horizontal") # check for horizontal collision
            self.hitbox.y += self.direction.y * speed # move the player hitbox by the direction * the speed
            self.collision("vertical") # check for vertical collision
            self.rect.center = self.hitbox.center # set the center of the player rect to the center of the player hitbox
        

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = sprite.hitbox.left # set the right side of the player hitbox to the left side of the obstacle hitbox
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = sprite.hitbox.right # set the left side of the player hitbox to the right side of the obstacle rect
        
        if direction == "vertical":
                for sprite in self.obstacle_sprites:
                    if sprite.hitbox.colliderect(self.hitbox):
                        if self.direction.y > 0: # moving down
                            self.hitbox.bottom = sprite.hitbox.top # set the bottom side of the player hitbox to the top side of the obstacle rect
                        if self.direction.y < 0: # moving up
                            self.hitbox.top = sprite.hitbox.bottom # set the top side of the player hitbox to the bottom side of the obstacle rect
    def update(self):
        self.input()
        self.move(self.speed) # move the player by the speed