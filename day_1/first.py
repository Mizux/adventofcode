#!/usr/bin/env python3

count = 0

f = open("input.txt", "r")
prev = int(f.readline())
for x in f:
    #print(f'current: {x}')
    x = int(x)
    if x > prev:
        count +=1
    prev = x

print(f'increase: {count}')
