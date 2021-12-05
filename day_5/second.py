#!/usr/bin/env python3
import re
from collections import defaultdict

FILE='test.txt' # sol: 12
FILE='input.txt' # sol: 21305

def parse_input(file):
    with open(file, 'r') as f:
        pattern = re.compile('(\d+),(\d+) -> (\d+),(\d+)')
        values = []
        for line in f:
            match = pattern.search(line)
            values.append([int(i) for i in match.groups()])
    return values


def is_diag(x1, y1, x2, y2):
    if abs(x2-x1) == abs(y2-y1):
        return True
    return False


values = parse_input(FILE)
#print(values)
wind = defaultdict(int)
for [x1, y1, x2, y2] in values:
    #print(f'{x1},{y1} -> {x2},{y2}')

    if x1 == x2:
        #print('vertical')
        for y in range(min(y1, y2), max(y1,y2)+1):
            wind[(x1, y)] += 1
            #print(f'wind[({x1}, {y})] += 1')
    elif y1 == y2:
        #print('horizontal')
        for x in range(min(x1, x2), max(x1, x2)+1):
            wind[(x, y1)] += 1
            #print(f'wind[({x}, {y1})] += 1')
    elif is_diag(x1, y1, x2, y2):
        #print('diagonal')
        x_dir = 1 if x1 < x2 else -1
        y_dir = 1 if y1 < y2 else -1
        delta = abs(x2-x1)+1
        for i in range(delta):
            x = x1 + i * x_dir
            y = y1 + i * y_dir
            wind[(x, y)] += 1
            #print(f'wind[({x}, {y})] += 1')
    else:
        #print('can\'t deal with it')
        continue

#print(wind)
count = 0
for _, value in wind.items():
    #print(key, value)
    if value > 1:
        count += 1
print(f'result: {count}')
