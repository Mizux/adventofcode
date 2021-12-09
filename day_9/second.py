#!/usr/bin/env python3
import numpy as np

FILE='test.txt' # sol: 9*14*9=1134
FILE='input.txt' # sol: 98*94*93=856716

def parse_input(file):
    board = []
    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip()
            #print(f'{line}')
            board.append([int(i) for i in line])
    #print(f'board: {board}')
    return board


def get_low_points(board):
    out = []
    for i in range(len(board)):
        for j in range(len(board[0])):
                val = board[i][j]
                if j-1 >= 0 and board[i][j-1] <= val:
                    continue
                if j+1 < len(board[i]) and board[i][j+1] <= val:
                    continue
                if i-1 >= 0 and board[i-1][j] <= val:
                    continue
                if i+1 < len(board) and board[i+1][j] <= val:
                    continue
                #print(f'risk at [{i},{j}]: {val}')
                out.append([i, j])
    #print(f'low points: {out}')
    return out


def get_bassin_size(board, point):
    count = 0
    to_check = [point]
    checked = set()
    while len(to_check) != 0:
        [i, j] = to_check.pop()
        if (i,j) in checked:
            continue
        checked.add((i, j))
        count += 1
        val = board[i][j]
        if j-1 >= 0 and board[i][j-1] < 9:
            to_check.append([i,j-1])
        if j+1 < len(board[i]) and board[i][j+1] < 9:
            to_check.append([i,j+1])
        if i-1 >= 0 and board[i-1][j] < 9:
            to_check.append([i-1,j])
        if i+1 < len(board) and board[i+1][j] < 9:
            to_check.append([i+1,j])
    #print(f'bassin{point} size: {count}')
    return count

def get_top3_bassin_size(board, low_points):
    out = []
    for point in low_points:
        out.append(get_bassin_size(board, point))
        if len(out) > 3:
            out.remove(min(out))
    print(f'top3 bassin sizes: {out}')
    return out

board = parse_input(FILE)
low_points = get_low_points(board)
out = get_top3_bassin_size(board, low_points)
print(f'result {np.prod(out)}')
