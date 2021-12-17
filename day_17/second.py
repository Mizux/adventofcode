#!/usr/bin/env python3
import re

FILE='test.txt' # sol: 112
FILE='input.txt' # sol: 2953

# regexp
def parse_input(file):
    with open(file, 'r') as f:
        pattern = re.compile('target area: x=(\d+)..(\d+), y=([-]\d+)..([-]\d+)')
        values = []
        for line in f:
            match = pattern.search(line)
            x1, x2, y1, y2 = [int(i) for i in match.groups()]
    #print(x1, x2, y1, y2)
    return x1, x2, y1, y2


def function(x1, x2, y1, y2, x_v, y_v):
    #print(f'testing vec: [{x_v},{y_v}]...')
    px, py = 0, 0
    max_y = 0
    while True:
        px += x_v
        py += y_v
        max_y= max(max_y, py)

        if x_v > 0:
            x_v -= 1
        elif x_v < 0:
            x_v += 1
        y_v -= 1
        if x1 <= px and px <= x2 and y1 <= py and py <= y2:
            #print(f'hit: [{px},{py}] (max: {max_y})')
            return max_y
        elif py < y1 or px > x2:
            #print(f'miss: [{px},{py}]')
            return None


x1, x2, y1, y2 = parse_input(FILE)
count = 0
velocities = []
for x_velocity in range(0, x2+1):
    for y_velocity in range(y1, abs(y1)):
      max_y = function(x1, x2, y1, y2, x_velocity, y_velocity)
      if max_y != None:
          count += 1
          velocities.append((x_velocity, y_velocity))

#print(f'initial states: {velocities}')
print(f'result: {count}')
