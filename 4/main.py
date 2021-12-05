import numpy as np
# import sys

class BingoGrid():
    def __init__(self, rows):
        self.rows = np.array(rows)
        self.dim = self.rows.shape
        self.marked_symbol = -1
        self.marking = np.zeros((len(self.rows), len(self.rows[0])))

    def mark(self, num):
        flat_rows = self.rows.flatten()
        flat_marking = self.marking.flatten()
        locations = np.where(flat_rows == num)[0]
        for loc in locations:
            flat_marking[loc] = self.marked_symbol
        self.marking = np.reshape(flat_marking, self.dim)


    def win_con(self, array):
        return len(list(filter(lambda x: x == self.marked_symbol, array))) == len(array)

    def is_won(self):
        for row in self.marking:
            if self.win_con(row):
                return True

        for i in range(self.dim[1]):
            col = self.marking[:,i]
            if self.win_con(col):
                return True
        return False

    # could have been done cleaner but got lazy
    def calculate_score(self, last_called):
        
        unmarked_total = 0
        
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if self.marking[i,j] != self.marked_symbol:
                    unmarked_total += self.rows[i,j]

        return unmarked_total * last_called


file_name = "input.txt"
f = open(file_name, "r")

drawn_numbers = f.readline()
drawn_numbers = list(map(lambda x: int(x), drawn_numbers.split(',')))


txt_inputs = f.readlines()
"""

'\n'

Then
5 numbers split by space then \n next to it
this is repeated 5 times 
"""

bingo_grids = []

for i in range(0, len(txt_inputs), 6):
    rows = []
    for j in range(1, 6):
        array = txt_inputs[i+j].strip().split()
        array = list(map(lambda x: int(x), array))
        rows.append(array)
    bingo_grids.append(BingoGrid(rows))

ans = None
for num in drawn_numbers:
    for grid in bingo_grids:
        grid.mark(num)
        if grid.is_won():
            print('pt.1')
            print(grid.calculate_score(num))
            ans = grid
            break
        
    if ans:
        break




print()
print('pt.2')
print()


ans = None
seen = []
for num in drawn_numbers:
    for i in range(len(bingo_grids)):
        if i in seen:
            continue
        grid = bingo_grids[i]

        grid.mark(num)
        if grid.is_won():
            seen.append(i)
            ans = grid
            if len(seen) == len(bingo_grids):
                print(seen)
                print(ans.rows)
                print(ans.marking)
                print(bingo_grids[seen[-1]].calculate_score(num))


