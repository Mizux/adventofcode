#!/usr/bin/env python3
import statistics as stat

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
        #cost += sum(range(abs(val - pos)+1))
    return cost


# split / rstrip()
def parse_input(file):
    with open(file, 'r') as f:
        k = f.readline().rstrip()
        #print(f'initial state: {k}')
        numbers = [int(i) for i in k.split(',')]
    return numbers


numbers = parse_input(FILE)
median = stat.median(numbers)
print(f'median: {median}')

min_idx = median
min_cost = count_cost(numbers, int(median))
print(f'result {min_cost}')
