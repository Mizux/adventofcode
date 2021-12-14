#!/usr/bin/env python3
import re

FILE='test.txt' # sol: 1588
FILE='input.txt' # sol: 2435

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


def apply_process(polymer, rules):
    out = ''
    for i in range(len(polymer)-1):
        out += polymer[i]
        pair = polymer[i]+polymer[i+1]
        if pair in rules:
            out += rules[pair]
    out += polymer[-1]
    return out


def get_stat(polymer):
    stat = {}
    for element in polymer:
        if element in stat:
            stat[element] += 1
        else:
            stat[element] = 1
    return stat


def get_min_max(stat):
    min_element = len(polymer)
    max_element = 0
    for element, frequence in stat.items():
        if frequence < min_element:
            min_element = frequence
        if frequence > max_element:
            max_element = frequence
    print(f'min: {min_element}, max:{max_element}')
    return min_element, max_element


polymer, rules = parse_input(FILE)
for i in range(10):
    polymer = apply_process(polymer, rules)
    #print(f'polymer[{i}]: {polymer} (len: {len(polymer)})')
stat = get_stat(polymer)
print(f'stat: {stat}')
min_element, max_element = get_min_max(stat)
print(f'result: {max_element - min_element}')
