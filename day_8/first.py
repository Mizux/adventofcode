#!/usr/bin/env python3

FILE='test.txt' # sol: 26
FILE='input.txt' # sol: 504

def parse_input(file):
    out = [];
    with open(file, 'r') as f:
        for line in f:
            digits = line.rstrip().split(" | ")[1].split(' ')
            #print(f'line digits: {digits}')
            out.extend(digits)
    #print(f'all digits: {out}')
    return out


entry = parse_input(FILE)
count = len([digit for digit in entry if len(digit) in [2, 4, 3, 7]]) # 1 4 7 8
print(f'result: {count}')
