import numpy as np
import copy 
from collections import defaultdict
from functools import reduce
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)
pprint = pp.pprint
# import sys

# helpers

def debug(x):
    print(x)
    print(type(x))

def convertToInts(lst):
    return list(map(int, lst))


file_name = "input.txt"
f = open(file_name, "r")

txt_inputs = f.read()
txt_inputs = txt_inputs.split('\n')
txt_inputs = [[int(digit) for digit in line] for line in txt_inputs]


""" 

Everyone increases by 1

Flashing

When an octopus flashes they effect all octopuses next to them (diag included).

123
456
678

If 5 flashes all numbers increase by 1.

Can only flash once a turn.

Count the amount of flahses

"""
def upgrade_neighbours(grid, x, y):
    movements = [1, 0, -1]
    n = len(grid)
    d = len(grid[0])

    for i in movements:
        for j in movements:
            if i == 0 and j == 0:
                continue
            new_x = x + i
            new_y = y + j
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= d:
                continue
            else:
                grid[new_x][new_y] += 1
    return grid

def apply_additions(grid, to_add):
    n = len(grid)
    d = len(grid[0])

    for i in range(n):
        for j in range(d):
            if grid[i][j] != None:
                grid[i][j] += to_add[i][j]
    return grid


def simulate_turn(grid):
    """ 
    Find all points where 9 exists 
    count the flash and then set val to None
    """
    n = len(grid)
    d = len(grid[0])

    flashes = 0

    # initial increase


    nines = 1
    # loop until no more 9s are seen
    while nines:
        to_add = [[0 for i in range(d)] for j in range(n)]
        nines = 0 
        for i in range(n):
            for j in range(d):
                val = grid[i][j]
                if val and val >= 9:
                    nines += 1
                    flashes += 1
                    grid[i][j] = None
                    to_add = upgrade_neighbours(to_add, i, j)
        grid = apply_additions(grid, to_add)

    to_add = [[1 for i in range(d)] for j in range(n)]
    grid = apply_additions(grid, to_add)
    
    # set state to next step
    for i in range(n):
        for j in range(d):
            val = grid[i][j]
            if val == None:
                grid[i][j] = 0
            
    return flashes, grid


ans = 0

for i in range(100):
    score, txt_inputs = simulate_turn(txt_inputs)
    ans += score

print('pt1')
print(ans)
print('pt2')


i = 100
goal = len(txt_inputs) * len(txt_inputs[0])
while True:
    score, txt_inputs = simulate_turn(txt_inputs)
    ans += score
    i += 1
    if score == goal:
        print(i)
        pprint(txt_inputs)
        break
