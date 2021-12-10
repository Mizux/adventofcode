#!/usr/bin/env python3

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

FILE='test.txt' # sol: 26397
FILE='input.txt' # sol: 358737

def get_parser_point(c):
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137


def parse_input(file):
    score = 0
    close_open_mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
            '>': '<'}
    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip()
            stack = []
            for c in line:
                if c in [')', ']', '}', '>']:
                    if len(stack) == 0:
                        score += get_parser_point(c)
                        break
                    if close_open_mapping[c] != stack.pop():
                        #print(f'line corrupted !')
                        stack = []
                        score += get_parser_point(c)
                        break
                else:
                    stack.append(c)
            if len(stack) != 0:
                #print(f'line incomplete !')
                #print(f'stack non empty! l:{line} s:{stack}')
                pass
            else:
                #print(f'line complete !')
                #print(f'l:{line}')
                pass
    #print(f'parsing score: {score}')
    return score


score = parse_input(FILE)
print(f'result: {score}')
