# need to create a file to help with importing the csv files to be useable
from csv import reader # allows use to read csv files

def import_csv_layout(path):
  with open(path) as level_map:
    layout = reader(level_map, delimiter = ',') # delimeter is what separates each entry in our file
    # similar to how to generate the basic rock map on level.py reference the create_map function
    for row in layout:
      print(row)


import_csv_layout('assets/map/map_FloorBlocks.csv')