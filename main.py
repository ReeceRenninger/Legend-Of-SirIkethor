import pygame, sys
from settings import *
from debug import debug
from level import Level

class Game:
  def __init__(self):

    # general setup of pygame off docs at https://www.pygame.org/docs/
    pygame.init()
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
    self.clock = pygame.time.Clock()
    pygame.display.set_caption('Adventure of Sir Ikethor') # changes the caption of the pygame window
  
    self.level = Level() # create a level object
    
  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      self.screen.fill('black') # generate a screen of just black
      # debug('hello :)') # debug the string 'hello :)' on the pygame screen, this can be used for testing in the future
      self.level.run() # run the level
      pygame.display.update() # update the display
      self.clock.tick(FPS) # set the FPS to 60 (FPS is a constant in settings.py)

if __name__ == '__main__':
  game = Game()
  game.run()