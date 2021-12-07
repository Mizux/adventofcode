#!/usr/bin/env python3
import re

FILE='test.txt' # sol: 37
FILE='input.txt' # sol:

def minmax(it):
    min = max = None
    for val in it:
        if min is None or val < min:
            min = val
        if max is None or val > max:
            max = val
    return min, max


def count_cost(it, pos):
    cost = 0
    for val in it:
        cost += abs(val - pos)
    return cost


# split / rstrip()
def parse_input(file):
    with open(file, 'r') as f:
        k = f.readline().rstrip()
        print(f'initial state: {k}')
        numbers = [int(i) for i in k.split(',')]
    return numbers


numbers = parse_input(FILE)
mi, ma = minmax(numbers)
print(f'min: {mi}, max {ma}')

min_idx = mi
min_cost = len(numbers) * ma

for i in range(mi, ma+1):
    c = count_cost(numbers, i)
    print(f'cost({i}): {c}')
    if c < min_cost:
        min_idx = i
        min_cost = c
print(f'result {min_cost}')
