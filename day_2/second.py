#!/usr/bin/env python3
import re

forward = 0
depth = 0
aim = 0

#f = open("test.txt", "r") # sol:900
f = open("input.txt", "r")

fw = re.compile('forward (\d+)')
up = re.compile('up (\d+)')
down = re.compile('down (\d+)')

for x in f:
    if fw.match(x):
        tmp = fw.search(x)
        forward += int(tmp.group(1))
        depth += aim * int(tmp.group(1))
    elif up.search(x):
        tmp = up.search(x)
        aim -= int(tmp.group(1))
    elif down.search(x):
        tmp = down.search(x)
        aim += int(tmp.group(1))
    else:
        print(f'unknow line "{x}"')

print(f'result: {forward * depth}')
