import numpy as np
# import sys


class Coord():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y
        return False



class LeftCord(Coord):
    pass
        


class RightCord(Coord):
    pass


class Grid():
    def __init__(self, min_x, max_x, min_y, max_y):
        self.x_diff = max_x - min_x
        self.y_diff = max_y - min_y
        self.array = np.zeros((self.x_diff + 1, self.y_diff + 1))
        self.diag_coord = []
        
    def mark_points_line(self, c1, c2):
        left_cord = c1
        right_cord = c2

        if (left_cord.x == right_cord.x):
            self.mark_horiz(left_cord.x, left_cord.y, right_cord.y)
        elif (left_cord.y == right_cord.y):
            self.mark_vert(left_cord.y, left_cord.x, right_cord.x)
        else:
            self.diag_coord.append((c1, c2))

    def mark_horiz(self, x, y1, y2):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        self.array[x, min_y:max_y + 1] += 1


    def mark_vert(self, y, x1, x2):
        min_x = min(x1, x2)
        max_x = max(x1, x2)

        self.array[min_x: max_x + 1, y] += 1

    def mark_diags(self):
        for cord in self.diag_coord:
            left = cord[0]
            right = cord[1]
            # should be diagnol
            assert(abs(left.x - right.x) == abs(right.y - left.y))
            # determine if the x,y increase or decreases (not neccessarily the same)
            x_step = 1 if left.x <= right.x else -1
            y_step = 1 if left.y <= right.y else -1
            
            self.array[right.x, right.y] += 1

            while (left != right):
                x = left.x
                y = left.y
                self.array[x,y] += 1
                left.x += x_step
                left.y += y_step

    def calc_pt1(self):

        total = 0
        n, d = self.array.shape
        for i in range(n):
            for j in range(d):
                val = self.array[i][j]
                if val > 1:
                    total += 1

        return total
    def calc_pt2(self):
        self.mark_diags()

        total = 0
        n, d = self.array.shape
        for i in range(n):
            for j in range(d):
                val = self.array[i][j]
                if val > 1:
                    total += 1

        return total


file_name = "input.txt"
f = open(file_name, "r")

txt_inputs = f.readlines()


"""
x1,x2 -> y1,y2

"""

coords = []

max_x = 0 
min_x = 0 
max_y = 0 
min_y = 0 

for line in txt_inputs:
    coord_split = line.split('->')
    left_cord = coord_split[0].strip()
    right_cord = coord_split[1].strip()

    right_coords = list(map(int, left_cord.split(',')))
    left_coords = list(map(int, right_cord.split(',')))

    left_cord = LeftCord(*right_coords)
    right_cord = RightCord(*left_coords)

    max_x = max(max_x, left_cord.x, right_cord.x)
    max_y = max(max_y, left_cord.y, right_cord.y)
    
    min_x = min(min_x, left_cord.x, right_cord.x)
    min_y = min(min_y, left_cord.y, right_cord.y)

    coords.append((left_cord, right_cord))

grid = Grid(min_x, max_x, min_y, max_y)

for cords in coords:
    left = cords[0]
    right = cords[1]

    grid.mark_points_line(left, right)

print('pt1')
print(grid.calc_pt1())

print()
print('pt2')
print(grid.calc_pt2())
