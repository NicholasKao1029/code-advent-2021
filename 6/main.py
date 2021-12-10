import numpy as np
from collections import defaultdict
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

fish = txt_inputs.split(',')
fish[-1] = fish[-1].strip()
fish = convertToInts(fish)

class FishAgeMap:
    def __init__(self, age_list):
        self.age_map = defaultdict(lambda: 0)
        for age in age_list:
            self.age_map[age] += 1

    def progressAge(self, days):
        for _ in range(days):
            self._progressOneDay()

    def _progressOneDay(self):
        RESET_VAL = 0
        NEW_AGE = 8 
        REBORN_AGE = 6
        
        temp_age_map = defaultdict(lambda: 0)

        for age in self.age_map:
            amount = self.age_map[age]
            # print(age)
            # print(amount)
            if age == RESET_VAL:
                temp_age_map[REBORN_AGE] += amount
                temp_age_map[NEW_AGE] += amount
            else:
                new_age = (age - 1) 
                temp_age_map[new_age] += amount


        # print(self.age_map)
        # print(temp_age_map)

        self.age_map = temp_age_map

    def total_fish(self):
        debug(self.age_map)
        debug(self.age_map.values())
        return sum(self.age_map.values())


fish_age_map = FishAgeMap(fish)
fish_age_map.progressAge(256)
print('pt1')
print(fish_age_map.total_fish())
print()
