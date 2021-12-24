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


"""
If a chunk opens with (, it must close with ).
If a chunk opens with [, it must close with ].
If a chunk opens with {, it must close with }.
If a chunk opens with <, it must close with >.

So, () is a legal chunk that contains no other chunks, as is []. More complex but valid chunks include ([]), {()()()}, <([{}])>, [<>({}){}[([])<>]], and even (((((((((()))))))))).

Some lines are incomplete, but others are corrupted. Find and discard the corrupted lines first.

A corrupted line is one where a chunk closes with the wrong character - that is, where the characters it opens and closes with do not form one of the four legal pairs listed above.

Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]). Such a chunk can appear anywhere within a line, and its presence causes the whole line to be considered corrupted.

if line is corrupted, return True
else return False
"""
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def get_score(symbol):
    closed_set = set(scores.keys())
    
    if symbol not in closed_set:
        raise Exception(f'symbol {symbol} not recognized')
    
    return scores[symbol]


def determine_corrupt_score(line):
    open = ['(', '[', '{', '<']
    open_set = set(open)
    closed = [')', ']', '}', '>']
    closed_set = set(closed)

    symbol_translation = dict(zip(closed, open))

    symbol_stack = []

    # if you see an open push it onto the stack
    # if you see a closed pop from the stack 
    # if they don't match 
    
    for sym in line:
        if sym in open_set:
            symbol_stack.append(sym)
        elif sym in closed_set:

            # without using a dictionary
            # sym_index = closed.index(sym)
            # correct_open = open[sym_index]

            correct_open = symbol_translation[sym]
            # edge case with empty stack 
            actual_open = symbol_stack.pop()

            if correct_open != actual_open:
                return get_score(sym)
        else:
            raise Exception(f'symbol {sym} not registerd')

    return 0


ans = 0
for line in txt_inputs:
    score = determine_corrupt_score(line)
    ans += score


print('pt1')
print(ans)
print('pt2')


def get_non_paried_symbols(line):
    open = ['(', '[', '{', '<']
    open_set = set(open)
    closed = [')', ']', '}', '>']
    closed_set = set(closed)

    symbol_translation = dict(zip(closed, open))

    symbol_stack = []

    # if you see an open push it onto the stack
    # if you see a closed pop from the stack 
    # if they don't match 
    
    for sym in line:
        if sym in open_set:
            symbol_stack.append(sym)
        elif sym in closed_set:
            # only takes incomplete non corrupt lines
            actual_open = symbol_stack.pop()
        else:
            raise Exception(f'symbol {sym} not registerd')

    return symbol_stack


def calc_incomplete_line_score(line):
    open = ['(', '[', '{', '<']
    open_set = set(open)
    closed = [')', ']', '}', '>']
    closed_set = set(closed)
    symbol_translation = dict(zip(open, closed))

    unpaired = get_non_paried_symbols(line)
    '''
    ): 1 point.
    ]: 2 points.
    }: 3 points.
    >: 4 points.
    '''

    score = 0
    def update_score(symbol, score):
        score *= 5
        score += (closed.index(symbol) +1)
        return score

    for sym in reversed(unpaired):
        if sym not in open_set:
            raise Exception(f'sym {sym} not in open symbol set')

        close_pair = symbol_translation[sym]
        score = update_score(close_pair, score)
    return score

incomplete_scores = []

for line in txt_inputs:
    score = determine_corrupt_score(line)
    if score == 0:
        score = calc_incomplete_line_score(line)
        incomplete_scores.append(score)


incomplete_scores.sort()
n = len(incomplete_scores)

middle_index = n//2
print(incomplete_scores[middle_index])
