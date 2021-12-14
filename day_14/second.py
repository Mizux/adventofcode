#!/usr/bin/env python3
import re

FILE='test.txt'  # sol: 2188189693529
FILE='input.txt' # sol: 2587447599164

def parse_input(file):
    with open(file, 'r') as f:
        polymer = f.readline().rstrip()
        #print(f'polymer template: {polymer}')

        f.readline();

        rules = {}
        pattern = re.compile('([A-Z]+)\s+->\s+([A-Z]+)')
        for line in f:
            match = pattern.search(line)
            pair = match.groups()[0]
            new = match.groups()[1]
            rules[pair] = new
        #print(f'rules: {rules}')

    return polymer, rules


def get_stat(polymer):
    '''Get stat of element without the last one'''
    stat = {}
    for c in polymer[:-1]:
        if c in stat:
            stat[c] += 1
        else:
            stat[c] = 1
    return stat


def merge_stat(stat_a, stat_b):
    stat = stat_a.copy()
    for c, freq in stat_b.items():
        if c in stat:
            stat[c] += freq
        else:
            stat[c] = freq
    return stat


memo = {}
def apply_process(step, pair, rules):
    if (step, pair) in memo:
        pass
    elif step > 0 and pair in rules:
        stat_a = apply_process(step-1, pair[0]+rules[pair], rules)
        stat_b = apply_process(step-1, rules[pair]+pair[1], rules)
        memo[(step, pair)] = merge_stat(stat_a, stat_b)
    else:
        memo[(step, pair)] = get_stat(pair)
    return memo[(step, pair)]


def get_min_max(stat):
    min_element = 2**40
    max_element = 0
    for element, frequence in stat.items():
        if frequence < min_element:
            min_element = frequence
        if frequence > max_element:
            max_element = frequence
    print(f'min: {min_element}, max:{max_element}')
    return min_element, max_element


polymer, rules = parse_input(FILE)
#print(f'polymer[{i}]: {polymer} (len: {len(polymer)})')
out = {}
for i in range(len(polymer)-1):
    pair = polymer[i]+polymer[i+1]
    stat = apply_process(40, pair, rules)
    out = merge_stat(out, stat)
# add last element
if polymer[-1] in out:
    out[polymer[-1]] += 1
else:
    out[polymer[-1]] = 1
print(f'stat: {out}')
min_element, max_element = get_min_max(out)
print(f'result: {max_element - min_element}')
