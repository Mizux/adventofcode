#!/usr/bin/env python3

SLIDE_WINDOWS = 3

f = open("input.txt", "r")
window = []
for i in range(SLIDE_WINDOWS):
    window.append(int(f.readline()))

count = 0
for cur in f:
    #print(f'current: {cur}')
    window.append(int(cur))
    if sum(window[1:]) > sum(window[0:-1]):
        count +=1
    window.pop(0)

print(f'increase: {count}')
