#!/usr/bin/env python3.10
from collections import defaultdict

FILE = 'test.txt'  # sol: 35
FILE='input.txt' # sol: 17096


def parse_input(file):
    with open(file, 'r') as f:
        table = f.readline().strip()
        assert len(table) == 2**9
        print(f'table: {table}')

        f.readline()

        board = []
        for line in f:
            board.append(line.rstrip())
        print(f'board:\n{to_string(board)}')
    return table, board


def to_string(board):
    string = ''
    for row in board:
        string += row +'\n'
    return string.rstrip()


def resize(board, n):
    width = len(board[0]) + 2 * n
    out = []
    for i in range(n):
        out.append('.' * width)
    for row in board:
        out.append('.' * n + row + '.' * n)
    for i in range(n):
        out.append('.' * width)
    #print(f'resized:\n{to_string(out)}')
    return out


def crop(board, n):
    out = []
    for row in board[n:-n]:
        out.append(row[n:-n])
    #print(f'croped:\n{to_string(out)}')
    return out


def enhance(table, board):
    output = []
    for i, row in enumerate(board):
        tmp = ''
        for j, _ in enumerate(row):
            tmp += compute_lit(table, board, i, j)
        output.append(tmp)
    #print(f'enhanced:\n{to_string(output)}')
    return output


def compute_lit(table, board, row, col):
    val = ''

    # top
    if row - 1 < 0:
        val = '000'
    else:
        ## left
        if col - 1 < 0:
            val += '0'
        else:
            val += '1' if board[row - 1][col - 1] == '#' else '0'
        ## middle
        val += '1' if board[row - 1][col] == '#' else '0'
        ## right
        if col + 1 < len(board[0]):
            val += '1' if board[row - 1][col + 1] == '#' else '0'
        else:
            val += '0'

    # middle
    ## left
    if col - 1 < 0:
        val += '0'
    else:
        val += '1' if board[row][col - 1] == '#' else '0'
    ## middle
    val += '1' if board[row][col] == '#' else '0'
    ## right
    if col + 1 < len(board[0]):
        val += '1' if board[row][col + 1] == '#' else '0'
    else:
        val += '0'

    # bottom
    if row + 1 >= len(board):
        val += '000'
    else:
        ## left
        if col - 1 < 0:
            val += '0'
        else:
            val += '1' if board[row + 1][col - 1] == '#' else '0'
        ## middle
        val += '1' if board[row + 1][col] == '#' else '0'
        ## right
        if col + 1 < len(board[0]):
            val += '1' if board[row + 1][col + 1] == '#' else '0'
        else:
            val += '0'

    assert len(val) == 9
    index = int(val, 2)
    return table[index]


def count_lit(board):
    count = 0
    for row in board:
        for c in row:
            if c == '#':
                count +=1
    return count


# Main
iteration = 50
table, board = parse_input(FILE)
board = resize(board, 2 * iteration + 1)
for i in range(iteration):
    board = enhance(table, board)
board = crop(board, iteration)
print(f'Final board:\n{to_string(board)}')
lit_number = count_lit(board)
print(f'result {lit_number}')
