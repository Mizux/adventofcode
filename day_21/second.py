#!/usr/bin/env python3.10
from collections import defaultdict
import re

FILE = 'test.txt'  # sol: 444356092776315
FILE='input.txt' # sol: 106768284484217

pattern = re.compile('Player (\d+) starting position: (\d+)')

def parse_input(file):
    players = dict()
    with open(file, 'r') as f:
        for line in f:
            match = pattern.search(line)
            players[int(match.group(1))] = int(match.group(2))
    #print(f'players: {players}')
    return players


memo = dict()
def play_game(players, scores, is_player1):
    key = (players[1], scores[1], players[2], scores[2], is_player1)
    if key in memo:
        return memo[key]

    if scores[1] >= 21:
        memo[key] = (1, 0)
    elif scores[2] >= 21:
        memo[key] = (0, 1)
    else:
        next_vals = defaultdict(int)
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    next_vals[i+j+k] += 1

        tmp_is_player1 = False if is_player1 else True

        result = (0, 0)
        for value, count in next_vals.items():
            tmp_players = players.copy()
            tmp_scores = scores.copy()
            if is_player1:
              tmp_players[1] = (players[1] + value - 1) % 10 + 1
              tmp_scores[1] += tmp_players[1]
            else:
              tmp_players[2] = (players[2] + value - 1) % 10 + 1
              tmp_scores[2] += tmp_players[2]
            tmp_result = play_game(tmp_players, tmp_scores, tmp_is_player1)
            result = (
                    result[0] + count * tmp_result[0],
                    result[1] + count * tmp_result[1])
        memo[key] = result
    return memo[key]


# Main
players = parse_input(FILE)
print(f'init: {players}')
scores = {1:0, 2:0}
print(f'scores: {scores}')
is_player1 = True

p1_win, p2_win = play_game(players, scores, is_player1)
print(f'p1_win: {p1_win}, p2_win: {p2_win}')

key = (players[1], scores[1], players[2], scores[2], is_player1)
print(f'result: {max(memo[key])}')
