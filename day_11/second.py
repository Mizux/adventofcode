#!/usr/bin/env python3

FILE='test.txt' # sol: all:195
FILE='input.txt' # sol: all:327

def print_board(board):
    for line in board:
        print(''.join([str(i) for i in line]))


def parse_input(file):
    board = []
    with open(file, 'r') as f:
        for line in f:
            board.append([int(i) for i in line.strip()])
    return board


def increase_energy(board):
    for line in board:
        for i in range(len(line)):
            line[i] += 1


def compute_flash(board):
    size = len(board)
    count = 0
    has_flash = True
    while has_flash:
        has_flash = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] > 9:
                    has_flash = True
                    count += 1
                    board[i][j] = -1
                    if j-1 >= 0 and board[i][j-1] != -1:
                        board[i][j-1] += 1
                    if j+1 < size and board[i][j+1] != -1:
                        board[i][j+1] += 1
                    if i-1 >= 0 and board[i-1][j] != -1:
                        board[i-1][j] += 1
                    if i+1 < size and board[i+1][j] != -1:
                        board[i+1][j] += 1
                    if j-1 >= 0 and i-1 >= 0 and board[i-1][j-1] != -1:
                        board[i-1][j-1] += 1
                    if i+1 < size and j+1 < size and board[i+1][j+1] != -1:
                        board[i+1][j+1] += 1
                    if i-1 >= 0 and j+1 < size and board[i-1][j+1] != -1:
                        board[i-1][j+1] += 1
                    if i+1 < size and j-1 >= 0 and board[i+1][j-1] != -1:
                        board[i+1][j-1] += 1
    for i in range(size):
        for j in range(size):
            if board[i][j] == -1:
                board[i][j] = 0
    return count


def all_flashed(board):
    all_flash = True
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                all_flash = False
                break
    return all_flash


def iterate(board):
    increase_energy(board)
    flash_count = compute_flash(board)
    return flash_count


board = parse_input(FILE)
print_board(board)
counter = 0
while True:
    if all_flashed(board):
        break
    counter += 1
    iterate(board)
    print(f'step {counter}')
print(f'result {counter}')
