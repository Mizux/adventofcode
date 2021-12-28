#!/usr/bin/env python3.10
from collections import defaultdict
import re

FILE = 'test.txt'  # sol: 39769202357779
FILE='input.txt' # sol: 1160303042684776

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
            rules.append({
                'on': light_on,
                'x1': x_min,
                'x2': x_max,
                'y1': y_min,
                'y2': y_max,
                'z1': z_min,
                'z2': z_max})
    #print(f'rules: {rules}')
    return rules


def parse_recipe(recipes):
    state = defaultdict(int)
    blocks = []

    for recipe in recipes:
        r = {
            'x1': recipe['x1'],
            'y1': recipe['y1'],
            'z1': recipe['z1'],
            'x2': recipe['x2'],
            'y2': recipe['y2'],
            'z2': recipe['z2'],
        }
        new_blocks = []
        for b in blocks:
            intersect = all([r['x1'] <= b['x2'], r['y1'] <= b['y2'], r['z1'] <= b['z2']]) and all([b['x1'] <= r['x2'], b['y1'] <= r['y2'], b['z1'] <= r['z2']])

            if not intersect:
                new_blocks.append(b)
                continue

            # x-axis
            if b['x1'] <= r['x2'] <= b['x2']:  # Positive direction
                new_blocks.append({
                    'x1': r['x2']+1,
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': b['z2'],
                })
                b = {
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': r['x2'],
                    'y2': b['y2'],
                    'z2': b['z2'],
                }
            if b['x1'] <= r['x1'] <= b['x2']:  # Negative direction
                new_blocks.append({
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': r['x1']-1,
                    'y2': b['y2'],
                    'z2': b['z2'],
                })
                b = {
                    'x1': r['x1'],
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': b['z2'],
                }
            # y-axis
            if b['y1'] <= r['y2'] <= b['y2']:  # Positive direction
                new_blocks.append({
                    'x1': b['x1'],
                    'y1': r['y2']+1,
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': b['z2'],
                })
                b = {
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': r['y2'],
                    'z2': b['z2'],
                }
            if b['y1'] <= r['y1'] <= b['y2']:  # Negative direction
                new_blocks.append({
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': r['y1']-1,
                    'z2': b['z2'],
                })
                b = {
                    'x1': b['x1'],
                    'y1': r['y1'],
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': b['z2'],
                }
            # z-axis
            if b['z1'] <= r['z2'] <= b['z2']:  # Positive direction
                new_blocks.append({
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': r['z2']+1,
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': b['z2'],
                })
                b = {
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': r['z2'],
                }
            if b['z1'] <= r['z1'] <= b['z2']:  # Negative direction
                new_blocks.append({
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': b['z1'],
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': r['z1']-1,
                })
                b = {
                    'x1': b['x1'],
                    'y1': b['y1'],
                    'z1': r['z1'],
                    'x2': b['x2'],
                    'y2': b['y2'],
                    'z2': b['z2'],
                }

        # Process the operation
        if recipe['on'] == True:
            new_blocks.append(r)
        blocks = new_blocks
    return blocks


def count_on(blocks):
    count = 0
    for b in blocks:
        count += (b['x2'] - b['x1'] + 1) * (b['y2'] - b['y1'] + 1) * (b['z2'] - b['z1'] + 1)
    return count


# Main
rules = parse_input(FILE)
#print(f'init: {rules}')
blocks = parse_recipe(rules)
count = count_on(blocks)
print(f'result: {count}')
