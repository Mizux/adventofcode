#!/usr/bin/env python3.10
from collections import defaultdict
import re

FILE = 'test.txt'  # sol: 590784
FILE='input.txt' # sol: 542711

pattern = re.compile('(on|off) x=([-]?\d+)..([-]?\d+),y=([-]?\d+)..([-]?\d+),z=([-]?\d+)..([-]?\d+)')

def parse_input(file):
    rules = []
    with open(file, 'r') as f:
        for line in f:
            match = pattern.search(line)
            #print(match)
            light_on = True if match.group(1) == 'on' else False
            x_min = int(match.group(2))
            x_max = int(match.group(3))
            y_min = int(match.group(4))
            y_max = int(match.group(5))
            z_min = int(match.group(6))
            z_max = int(match.group(7))
            #print(f'line: {light_on}, x:[{x_min},{x_max}], y:[{y_min},{y_max}], z:[{z_min},{z_max}]')
            rules.append((light_on, x_min, x_max, y_min, y_max, z_min, z_max))
    #print(f'rules: {rules}')
    return rules


def parse_recipe(recipes):
    state = defaultdict(int)
    for recipe in recipes:
        for x in range(max(-50, recipe[1]), min(50, recipe[2])+1):
            for y in range(max(-50, recipe[3]), min(50, recipe[4])+1):
                for z in range(max(-50, recipe[5]), min(50, recipe[6])+1):
                    state[(x, y, z)] = recipe[0]
    return state


def count_on(state):
    count = 0
    for _, val in state.items():
        count += 1 if val == True else 0
    return count


# Main
rules = parse_input(FILE)
#print(f'init: {rules}')
state = parse_recipe(rules)
count = count_on(state)
print(f'result: {count}')
