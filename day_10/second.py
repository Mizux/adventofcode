#!/usr/bin/env python3

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

FILE='test.txt' # sol: 288957
FILE='input.txt' # sol: 4329504793

def get_parser_point(c):
    #print(f'char: {c}')
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137


def get_checker_point(c):
    #print(f'char: {c}')
    if c == '(':
        return 1
    if c == '[':
        return 2
    if c == '{':
        return 3
    if c == '<':
        return 4


# split / rstrip()
def parse_input(file):
    incomplete = []
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
                    continue
            if len(stack) != 0:
                #print(f'line incomplete !')
                #print(f"stack non empty!!!! l:{line} st:{''.join(stack)}")
                incomplete.append([line, stack])
            else:
                #print(f'line complete !')
                #print(f'l:{line}')
                pass
    #print(f'parsing score: {score}')
    #print(f'incomplete: {incomplete}')
    return incomplete


def syntax_checker(incomplete):
    #print(f'nb of incomlete lines: {len(incomplete)}')
    scores = []
    for [line, stack] in incomplete:
        score = 0
        while len(stack) != 0:
            score = 5 * score + get_checker_point(stack.pop())
        #print(f'checker line score: {score}')
        scores.append(score)
    #print(f"checker scores: {scores}")
    return sorted(scores)


incomplete = parse_input(FILE)
scores = syntax_checker(incomplete)
print(f'result {scores[len(scores)//2]}')
