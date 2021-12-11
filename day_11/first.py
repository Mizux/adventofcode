#!/usr/bin/env python3

FILE='test.txt' # sol: 10:204 100:1656
FILE='input.txt' # sol: 100:1723

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


def iterate(board):
    increase_energy(board)
    flash_count = compute_flash(board)
    return flash_count


board = parse_input(FILE)
print_board(board)
flash_count = 0
for i in range(100):
    flash_count += iterate(board)
    print(f'step {i} flash:{flash_count}')
print(f'result {flash_count}')
