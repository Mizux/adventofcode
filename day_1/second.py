#!/usr/bin/env python3

count = 0

f = open("input.txt", "r")
a_one = int(f.readline())
a_two = int(f.readline())
a_three = int(f.readline())

b_one = a_two
b_two = a_three
b_three = 0
for x in f:
    print(f'current: {x}')
    b_three = int(x)

    if sum([b_one, b_two, b_three]) > sum([a_one, a_two, a_three]):
        count +=1
    a_one = a_two
    a_two = a_three
    a_three = b_three
    b_one = b_two
    b_two = b_three
    b_three = 0

print(f'increase: {count}')
