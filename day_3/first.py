#!/usr/bin/env python3

#FILE='test.txt' # sol = 198
#WORD_SIZE=5
FILE='input.txt' # sol: 394*3701=1458194
WORD_SIZE=12

gamma = 0
epsilon = 0
with open(FILE, 'r') as f:
    bit_count = [0] * WORD_SIZE
    for line in f:
        number = int(line, base=2)
        #print(f'number: {number}')
        for i in range(WORD_SIZE):
            mask = 0x1 << i
            if number & mask:
                bit_count[i] += 1
            else:
                bit_count[i] -= 1
    #print(f'counter: {bit_count}')
    for i in range(WORD_SIZE):
        if bit_count[i] > 0:
            gamma += (0x1 << i)
print(f'gamma: {gamma}')

epsilon = gamma ^ (pow(2, WORD_SIZE) - 1)
print(f'epsilon: {epsilon}')

print(f'result: {gamma * epsilon}')
