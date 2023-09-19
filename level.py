import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
  def __init__(self):

    # get the display surface
    self.display_surface = pygame.display.get_surface()

    # sprite group setup
    self.visible_sprites = CameraGroup()
    self.obstacle_sprites = pygame.sprite.Group()

    # sprite setup
    self.create_map()

  def create_map(self):
    for row_index, row in enumerate(WORLD_MAP): # enumerate gives us the index and the value of the item in the list
      for col_index, col in enumerate(row): 
          x = col_index * TILESIZE # x position is the column index * the tilesize
          y = row_index * TILESIZE # y position is the row index * the tilesize
          if col == 'x': # if the value of the column is 'x' then create a tile at that position
            Tile((x, y), [self.visible_sprites, self.obstacle_sprites]) # generating rocks, visible and obstacle
          if col == 'p': # if the value of the column is 'p' then create player tile at that position
            self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites) # generating player

  def run(self):
    #update and draw the game
   
    self.visible_sprites.custom_draw(self.player) # custom draw does the offset for the camera
    self.visible_sprites.update() # update the visible sprites

    debug(self.player.direction) #! remove before release

class CameraGroup(pygame.sprite.Group):
  def __init__(self):
    #setup the camera
    super().__init__()
    self.display_surface = pygame.display.get_surface() # get the display surface
    self.half_width = self.display_surface.get_width() // 2 # get the half width of the display surface
    self.half_height = self.display_surface.get_height() // 2 # get the half height of the display surface
    self.offset = pygame.math.Vector2(0, 0) # set the offset to 0, 0 for sprite overlap offset

  def custom_draw(self, player):
    # get offset
    self.offset.x = player.rect.centerx - self.half_width # player.rect.centerx is the center of the player sprite on x
    self.offset.y = player.rect.centery - self.half_height # player.rect.centery is the center of the player sprite on y
    for sprite in self.sprites(): # loop through all the sprites in the group
      offset_sprite_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image, offset_sprite_pos) # draw the sprite to the display surface with offset