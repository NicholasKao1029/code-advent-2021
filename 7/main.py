import numpy as np
from collections import defaultdict
import statistics 
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
txt_inputs = txt_inputs.split(',')
txt_inputs[-1] = txt_inputs[-1].strip()
txt_inputs = convertToInts(txt_inputs)
max_input = max(txt_inputs)

rounded_mean = (round(statistics.mean(txt_inputs)))


def calcPriceNaive(alignment_pos, positions):
    total = 0

    for pos in positions:
        total += abs(pos - alignment_pos)

    return total

mean_pos_cost = (calcPriceNaive(rounded_mean, txt_inputs))

def find_min_by_cost_func(cost_func):
    min_cost = float('inf')
    min_cost_pos = 0
    for i in range(max_input):
        curr_cost = cost_func(i, txt_inputs)
        if curr_cost < min_cost:
            min_cost = curr_cost
            min_cost_pos = i
    return min_cost, min_cost_pos

min_cost_niave, min_cost_pos_niave = find_min_by_cost_func(calcPriceNaive)

print('pt1')
print(f'min cost is {min_cost_niave} at position {min_cost_pos_niave}')
print()



def calcPriceCrabEngineering(alignment_pos, positions):
    total = 0
    def triangle_number(n):
        return n * (n + 1) // 2

    for pos in positions:
        total += triangle_number(abs(pos - alignment_pos))

    return total

min_cost_sophisticated, min_cost_pos_sophisticated = find_min_by_cost_func(calcPriceCrabEngineering)



print('pt2')
print(f'min cost is {min_cost_sophisticated} at position {min_cost_pos_sophisticated}')
