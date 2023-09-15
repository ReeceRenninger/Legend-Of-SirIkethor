import pygame

pygame.init()

font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
  display_surface = pygame.display.get_surface() # get the display surface for the screen
  debug_surf = font.render(str(info), True, 'White') # render the debug info to a surface with the font and color of white
  debug_rect = debug_surf.get_rect(topleft = (x, y)) # get the rect of the debug surface
  pygame.draw.rect(display_surface, 'black', debug_rect) # draw a black rectangle over the debug info
  display_surface.blit(debug_surf, debug_rect) # blit the debug surface to the display surface