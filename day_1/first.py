#!/usr/bin/env python3

count = 0

f = open("input.txt", "r")
prev = 10_000
for x in f:
    print(f'current: {x}')
    if int(x) > prev:
        count +=1
    prev = int(x)

print(f'increase: {count}')
