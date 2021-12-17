import numpy as np
import copy 
from collections import defaultdict
from functools import reduce
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


graph = []

for s in txt_inputs:
    x = convertToInts(list(s))
    graph.append(x)



# return all valid neighbours of point i j on graph
def look_around(i, j, graph):
    neighbours = []
    n = len(graph)
    d = len(graph[0])

    possibilities = [-1,1]

    # change i 
    for p in possibilities:
        new = i + p
        if new < 0 or new >=n:
            continue
        neighbours.append([new, j])
        
        
    # change j 
    for p in possibilities:
        new = j + p
        if new < 0 or new >=n:
            continue
        neighbours.append([i, new])
        
    return neighbours



n = len(graph)
d = len(graph[0])

low_points = []
low_point_cord = []

for i in range(n):
    for j in range(d):
        cur_val = graph[i][j]
        neighbours = look_around(i,j, graph)

        is_smallest = True
        for n in neighbours:
            point = graph[n[0]][n[1]]
            if point <= cur_val:
                is_smallest = False
                break

        if is_smallest:
            low_points.append(cur_val)
            low_point_cord.append([i,j])


print('pt1')
ans = sum([(lp + 1) for lp in low_points])
print(ans)
print()





def calc_basin_size(i,j):
    graph_copy = copy.deepcopy(graph)
    # get the point
    # mark as seen
    # look at neighbours that are larger (will always exist for first point)
    # for each of those points look at their neighbours and determine if they are larger 
    # queue structure?
    # 9 is never part of a basin


for lpc in low_point_cord:
    basin = calc_basin_size(lpc[0], lpc[1])


print('pt2')
