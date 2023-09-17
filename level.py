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
    self.visible_sprites = pygame.sprite.Group()
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
            self.player = Player((x, y), [self.visible_sprites]) #generating player

  def run(self):
    #update and draw the game
    # pass # not doing anything yet
    self.visible_sprites.draw(self.display_surface) # draw the visible sprites to the display surface
    self.visible_sprites.update() # update the visible sprites
    debug(self.player.direction)