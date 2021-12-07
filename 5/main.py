import numpy as np
# import sys


class Coord():
    def __init__(self, one, two):
        self.one = one
        self.two = two


class XCoord(Coord):
    pass
        


class YCoord(Coord):
    pass


class Grid():
    def __init__(self, min_x, max_x, min_y, max_y):
        pass


file_name = "input.txt"
f = open(file_name, "r")

txt_inputs = f.readlines()


"""
x1,x2 -> y1,y2

"""

coords = []

for line in txt_inputs:
    coord_split = line.split('->')
    x = coord_split[0].strip()
    y = coord_split[1].strip()

    x_coords = x.split(',')
    y_coords = y.split(',')

    x_cord = XCoord(*x_coords)
    y_cord = YCoord(*y_coords)

    coords.append((x_cord, y_cord))
