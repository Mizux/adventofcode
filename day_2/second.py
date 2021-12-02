#!/usr/bin/env python3
import re

forward = 0
depth = 0
aim = 0

#f = open("test.txt", "r") # sol:900
f = open("input.txt", "r")

pattern = re.compile('(\w+) (\d+)')

for line in f:
    match = pattern.search(line)
    command = match.group(1)
    x = int(match.group(2))

    if command == 'forward':
        forward += x
        depth += aim * x
    elif command == 'up':
        aim -= x
    elif command == 'down':
        aim += x
    else:
        print(f'unknow command "{command}"')

print(f'result: {forward * depth}')
