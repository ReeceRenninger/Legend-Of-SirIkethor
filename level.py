import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from helper import *

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
    layout = {
          'boundary' : import_csv_layout('assets/map/map_FloorBlocks.csv')
    }
    #!! indentation is key here, if the indentation is off then the code will not work properly with reading the floor blocks csv file
    for style, layout in layout.items(): # style is representative of the boundary while layout is representative of the map_FloorBlocks.csv
      for row_index, row in enumerate(layout): # enumerate gives us the index and the value of the item in the list
          for col_index, col in enumerate(row): 
              if col != '-1': # if the value of the column is not -1 then create a tile at that position, csv file is outputting -1 for empty spaces
                  x = col_index * TILESIZE # x position is the column index * the tilesize
                  y = row_index * TILESIZE # y position is the row index * the tilesize
                  if style == 'boundary':
                      Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'invisible') #position is the x,y position, groups is the visible and obstacle sprites, sprite_type is invisible. These are tile parameters from tile.py modified for the boundary
    #       if col == 'x': # if the value of the column is 'x' then create a tile at that position
    #         Tile((x, y), [self.visible_sprites, self.obstacle_sprites]) # generating rocks, visible and obstacle
    #       if col == 'p': # if the value of the column is 'p' then create player tile at that position
    #         self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites) # generating player
     #** Creating a new player position with the actual map
      self.player = Player((1275, 1950), [self.visible_sprites], self.obstacle_sprites) # generating player

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

    # create the floor from the bottom of the screen using tile image
    self.floor_surface = pygame.image.load('assets/ground/ground.png').convert() # load the tile image
    self.floor_rect = self.floor_surface.get_rect(topleft = (0,0))

  def custom_draw(self, player):
    # get offset
    self.offset.x = player.rect.centerx - self.half_width # player.rect.centerx is the center of the player sprite on x
    self.offset.y = player.rect.centery - self.half_height # player.rect.centery is the center of the player sprite on y
   
    # draw the floor
    floor_offset_pos = self.floor_rect.topleft - self.offset # get the offset position of the floor
    self.display_surface.blit(self.floor_surface, floor_offset_pos) # draw the floor to the display surface with offset

    for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery): # loop through all the sprites in the group, sorted by the y position of the sprite
      offset_sprite_pos = sprite.rect.topleft - self.offset
      self.display_surface.blit(sprite.image, offset_sprite_pos) # draw the sprite to the display surface with offset