# need to create a file to help with importing the csv files to be useable
from csv import reader # allows use to read csv files
from os import walk # allows us to walk through a folder


def import_csv_layout(path):
  terrain_map = []
  with open(path) as level_map:
    layout = reader(level_map, delimiter = ',') # delimeter is what separates each entry in our file
    # similar to how to generate the basic rock map on level.py reference the create_map function instead of iterating the entire map variable we are iterating the csv file itself
    for row in layout:
        terrain_map.append(list(row)) # append each row to the terrain map and keep it set up as a list for each row
    return terrain_map

def import_folder(path):
   # iterate through folder to import all the grass or objects or w/e we need 
    for data in walk(path):
       print(data) 

import_folder('assets/graphics/grass') # test to see if the folder is being read properly
# print(import_csv_layout('assets/map/map_FloorBlocks.csv')) # test to see if the csv file is being read properly