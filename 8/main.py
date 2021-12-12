import numpy as np
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


class Display:
    def __init__(self, first, output):
        self.first = first
        self.output = output


displays = []

for i in range(len(txt_inputs)):
    line = txt_inputs[i]
    line_split = line.split(' | ')
    display = Display(*line_split)
    displays.append(display)

num_section_map = {
    0:6,
    1:2,
    2:5,
    3:5,
    4:4,
    5:5,
    6:6,
    7:3,
    8:7,
    9:6
}



unique_len_digits = set([1,4,7,8])
unique_lengths = [num_section_map[x] for x in unique_len_digits]
debug(unique_lengths)



def calc_num_output_digits_unique_length(displays):
    total = 0
    for display in displays:
        output = display.output
        digit_list = output.split()
        for digit in digit_list: 
            if len(digit) in unique_lengths:
                total += 1
    return total

total = calc_num_output_digits_unique_length(displays)

print('pt1')
print(total)
print()


# amount_of_section_map = {
#     6:0,
#     6:6,
#     6:9,
#     5:2,
#     5:3,
#     5:5,
#     2:1,
#     4:4,
#     3:7,
#     7:8,
# }

def calculate_0(seven, one):
    print(seven, one)
    return (set(seven) - set(one)).pop()

def calculate_6(len_5, zero, one, a):
    sets_len_5 = [set(jumble) for jumble in len_5]

    def reduce_func(something, next):
        return something.intersection(next)
    
    common_intersection = reduce(reduce_func, sets_len_5)
    
    three = None
    two_five = []

    for set_obj in sets_len_5:
        difference = set_obj - common_intersection
        if difference == set(one):
            three = set_obj
        else:
            two_five.append(set_obj)

    some_diff = (two_five[0] - common_intersection) 
    some_diff = some_diff - set(one)
    eb_set = some_diff - (two_five[1] - common_intersection)

    sides = eb_set.union(one)
    ag_set = set(zero) - sides

    return (ag_set - a).pop()

# takes in an input line from a display
def calculate_wiring(input):
    n = len(input)
    assert(n == 10)

    digit_to_string = [0] * n

    length_6 = []
    length_5 = []

    wire_config = [0] * 7
    for jumble in input:
        jumble_len = len(jumble)
        if jumble_len == 7:
            digit_to_string[8] = jumble
        elif jumble_len == 3:
            digit_to_string[7] = jumble
        elif jumble_len == 4:
            digit_to_string[4] = jumble
        elif jumble_len == 2:
            digit_to_string[1] = jumble
        elif jumble_len == 5:
            length_5.append(jumble)
        elif jumble_len == 6:
            length_6.append(jumble)
        
    wire_config[0] = calculate_0(digit_to_string[7], digit_to_string[1])
    wire_config[6] = calculate_6(length_5, digit_to_string[0], digit_to_string[1], wire_config[0])

    return wire_config



print(calculate_wiring("fbead dcabe bcega gfbecd ecd dgac cd bedcag agebcfd fcagbe".split()))


