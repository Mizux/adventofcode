#!/usr/bin/env python3
import statistics as stat

FILE='test.txt' # sol: 168
FILE='input.txt' # sol: 100220525

def minmax(it):
    min = max = None
    for val in it:
        if min is None or val < min:
            min = val
        if max is None or val > max:
            max = val
    return min, max


def arithmetic_series(start, stop, step=1):
    number_of_terms = (stop - start) // step
    sum_of_extrema = start + (stop - step)
    return number_of_terms * sum_of_extrema // 2


def get_cost(it, target):
    cost = 0
    for val in it:
        cost += arithmetic_series(0, abs(val - target)+1)
    return cost


# split / rstrip()
def parse_input(file):
    with open(file, 'r') as f:
        k = f.readline().rstrip()
        #print(f'initial state: {k}')
        numbers = [int(i) for i in k.split(',')]
    return numbers


numbers = parse_input(FILE)

# MEAN
mean = stat.mean(numbers)
print(f'mean: {mean}')
target = int(mean)
min_cost = get_cost(numbers, target)
print(f'result: target:{target} fuel:{min_cost}')

# MEDIAN
median = stat.median(numbers)
print(f'median: {median}')
target = int(median)
min_cost = get_cost(numbers, target)
print(f'result: target:{target} fuel:{min_cost}')

# BRUTE FORCE
#mi, ma = minmax(numbers)
#print(f'min: {mi}, max {ma}')
#target = mi
#min_cost = len(numbers) * sum(range(ma+1))
#for i in range(mi, ma+1):
#    c = get_cost(numbers, i)
#    print(f'cost({i}): {c}')
#    if c < min_cost:
#        target = i
#        min_cost = c
#print(f'result: idx:{target} fuel:{min_cost}')
