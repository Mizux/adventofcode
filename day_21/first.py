#!/usr/bin/env python3.10
from collections import defaultdict
import re

FILE = 'test.txt'  # sol: 739785
FILE='input.txt' # sol: 1196172

pattern = re.compile('Player (\d+) starting position: (\d+)')

def parse_input(file):
    players = dict()
    with open(file, 'r') as f:
        for line in f:
            match = pattern.search(line)
            players[int(match.group(1))] = int(match.group(2))
    #print(f'players: {players}')
    return players


def play_game(players):
    p1 = players[1]
    p1_score = 0
    p2 = players[2]
    p2_score = 0

    roll = 0
    dice = 1
    is_p1 = True
    while p1_score < 1000 and p2_score < 1000:
        roll += 3
        val = 3 * dice + 3
        if is_p1:
            p1 = (p1 + val - 1) % 10 + 1
            p1_score += p1
        else:
            p2 = (p2 + val - 1) % 10 + 1
            p2_score += p2
        dice = (dice + 3 - 1) % 100 + 1
        is_p1 = False if is_p1 else True

    print(f'p1: {p1_score}')
    print(f'p2: {p2_score}')
    print(f'roll: {roll}')
    return roll, min(p1_score, p2_score)


# Main
players = parse_input(FILE)
print(f'init: {players}')
roll, min_score = play_game(players)
assert roll % 3 == 0

value = roll * min_score
print(f'result: {value}')
