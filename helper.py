# need to create a file to help with importing the csv files to be useable
from csv import reader # allows use to read csv files
from os import walk # allows us to walk through a folder
import pygame

def import_csv_layout(path):
  terrain_map = []
  with open(path) as level_map:
    layout = reader(level_map, delimiter = ',') # delimeter is what separates each entry in our file
    # similar to how to generate the basic rock map on level.py reference the create_map function instead of iterating the entire map variable we are iterating the csv file itself
    for row in layout:
        terrain_map.append(list(row)) # append each row to the terrain map and keep it set up as a list for each row
    return terrain_map

def import_folder(path):
    surface_list = [] # create a list to store the surfaces
   # iterate through folder to import all the grass or objects or w/e we need 
    for _,__,img_files in walk(path): # walk through the path and get the image files, the _ and __ are for the root and directories which we don't need to name, saw this in a tutorial
        for image in img_files: # iterate through the image files
            full_path = path + '/' + image # create the full path to the image to easily import it
            image_surf = pygame.image.load(full_path).convert_alpha() # load the image and convert it to alpha from the docs
            surface_list.append(image_surf) # append the image to the surface list
    return surface_list

# import_folder('assets/graphics/grass') # test to see if the folder is being read properly
# print(import_csv_layout('assets/map/map_FloorBlocks.csv')) # test to see if the csv file is being read properly