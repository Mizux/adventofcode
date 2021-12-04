#!/usr/bin/env python3

BOARD_SIZE=5
#FILE='test.txt' # sol: 188*24=4512
FILE='input.txt' # sol: 11536

def parse_input(file):
    with open(file, 'r') as f:
        numbers = [int(i) for i in f.readline().rstrip().split(',')]
        f.readline() #  ignore first empty line

        boards = []
        grid = []
        for line in f:
            line = line.rstrip()
            if line == '': # grids are separated by empty line
                boards.append(grid)
                grid = []
                continue
            tmp = [int(i) for i in line.split()]
            assert len(tmp) == BOARD_SIZE
            grid.append(tmp)
        boards.append(grid) # don't forget to add last grid
    #print(f'numbers: {numbers}')
    #print(f'boards: {boards}')
    return [numbers, boards]


def remove_number(boards, nb):
    for grid in boards:
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if grid[row][col] == nb:
                    grid[row][col] = -1


def check_boards(boards):
    for idx, grid in enumerate(boards):
        #print(f'check grid: {grid}')
        # check horizontal bingo
        for row in range(BOARD_SIZE):
            found = True
            for col in range(BOARD_SIZE):
                value = grid[row][col]
                #print(f'check value[{row},{col}]: {value}')
                if value != -1:
                    found = False
                    break
            if found:
                return [found, idx]
        # check vertical bingo
        for col in range(BOARD_SIZE):
            found = True
            for row in range(BOARD_SIZE):
                value = grid[row][col]
                #print(f'check value[{row},{col}]: {value}')
                if value != -1:
                    found = False
                    break
            if found:
                return [found, idx]
    return [False, None]


def grid_sum(grid):
    grid_sum = 0
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if grid[row][col] != -1:
                grid_sum += grid[row][col]
    return grid_sum


[numbers, boards] = parse_input(FILE)
for number in numbers:
    #print(f'number: {number}')
    remove_number(boards, number)
    res = check_boards(boards)
    if res[0]:
        total = grid_sum(boards[res[1]])
        print(f'result: {number * total}')
        exit(0)
