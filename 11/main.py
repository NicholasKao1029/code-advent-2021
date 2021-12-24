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


