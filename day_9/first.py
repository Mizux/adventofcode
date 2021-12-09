#!/usr/bin/env python3

FILE='test.txt' # sol: 15
FILE='input.txt' # sol: 580

# split / rstrip()
def parse_input(file):
    board = []
    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip()
            print(f'{line}')
            board.append([int(i) for i in line])
    print(f'board: {board}')
    return board


def function(board):
    out = 0
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
                print(f'risk at [{i},{j}]: {val}')
                out += val +1
    return out
    print(f'res: {out}')
    return out


board = parse_input(FILE)
out = function(board)
print(f'result {out}')
