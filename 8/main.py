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

# takes in an input line from a display
# will produce number to corresponding jumble
def calculate_number(input):
    input = input.split()
    n = len(input)
    assert(n == 10)

    num_to_jumble = [0] * n

    length_6 = []
    length_5 = []

    for jumble in input:
        jumble_len = len(jumble)
        if jumble_len == 7:
            num_to_jumble[8] = jumble
        elif jumble_len == 3:
            num_to_jumble[7] = jumble
        elif jumble_len == 4:
            num_to_jumble[4] = jumble
        elif jumble_len == 2:
            num_to_jumble[1] = jumble
        elif jumble_len == 5:
            length_5.append(jumble)
        elif jumble_len == 6:
            length_6.append(jumble)

    two, three, five = handle_len_5(length_5, num_to_jumble[1], num_to_jumble[4])
    num_to_jumble[2] = two
    num_to_jumble[3] = three 
    num_to_jumble[5] = five

    zero, six, nine = handle_len_6(length_6, num_to_jumble[1], num_to_jumble[5])

    num_to_jumble[0] = zero
    num_to_jumble[6] = six 
    num_to_jumble[9] = nine

    return num_to_jumble

# takes in list of jumbles with length 5
def handle_len_5(jumbles, one, four):
    two = None
    three = None
    five = None

    set_len_5 = {j:set(j) for j in jumbles }

    def reduce_func(something, next):
        return something.intersection(next)
    
    common_intersection = reduce(reduce_func, set_len_5.values()) # should only contain a d g

    assert(len(common_intersection) == 3)
    leftovers = {s:(set_len_5[s] - common_intersection) for s in set_len_5 }

    # intersect with one 
    # if length left is 
        # 2 it's three
        # 1 it's two 
        # 0 it's five

    three_or_five = []

    for l in leftovers:
        leftover_set = leftovers[l]
        intersect = leftover_set.intersection(one)
        if len(intersect) == 1:
            three_or_five.append(l)
        if len(intersect) == 2:
            three = l

    four_set = set(four)
    four_set = four_set - set(one)
    four_set = four_set - (four_set.intersection(common_intersection))

    assert(len(four_set) == 1)

    for x in three_or_five:
        sett = leftovers[x]
        diff = sett - four_set
        if len(diff) == 1:
            five = x
        else:
            assert(len(diff) == 2)
            two = x

    return two, three, five

def handle_len_6(jumbles, one, five):
    zero = None
    six = None
    nine = None

    five_set = set(five)
    one_set = set(one)

    set_len_6 = {j:set(j) for j in jumbles }

    for s in set_len_6:
        sett = set_len_6[s]
        diff = sett - five_set

        if len(diff) == 2:
            zero = s
        else:
            assert(len(diff) == 1)
            something = one_set - diff
            if len(something) == 1:
                nine = s
            elif len(something) == 2:
                six = s


    return zero, six, nine


print(calculate_number(displays[0].first))


def part2():
    ans = 0
    for display in displays:
        input = display.first
        code = display.output.split()
        code = [set(s) for s in code]

        translation = calculate_number(input)
        translation = [set(x) for x in translation]

        output = "" 
        for c in code:
            num = translation.index(c)
            output += str(num)
        ans += int(output)
    return ans


print('pt2')
ans = part2()
print(ans)

