#!/usr/bin/env python3

BOARD_SIZE = 5
SENTINEL = -1
#FILE='test.txt' # sol: 148 * 13 = 1924
FILE='input.txt' # sol: 6 * 214 = 1284

def parse_input(file):
    with open(file, 'r') as f:
        numbers = [int(i) for i in f.readline().rstrip().split(',')]
        f.readline() #  ignore first empty line

        boards = []
        grid = []
        for line in f:
            line = line.rstrip()
            if line == '': # grids are separated by empty line
                assert len(grid) == BOARD_SIZE
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
                    grid[row][col] = SENTINEL


def check_grid(grid):
    # check horizontal bingo
    for row in range(BOARD_SIZE):
        found = True
        for col in range(BOARD_SIZE):
            value = grid[row][col]
            #print(f'check value[{row},{col}]: {value}')
            if value != SENTINEL:
                found = False
                break
        if found:
            return True
    # check vertical bingo
    for col in range(BOARD_SIZE):
        found = True
        for row in range(BOARD_SIZE):
            value = grid[row][col]
            #print(f'check value[{row},{col}]: {value}')
            if value != SENTINEL:
                found = False
                break
        if found:
            return True
    return False


def grid_sum(grid):
    grid_sum = 0
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if grid[row][col] != SENTINEL:
                grid_sum += grid[row][col]
    return grid_sum


[numbers, boards] = parse_input(FILE)
for number in numbers:
    remove_number(boards, number)
    for grid in boards:
        has_bingo = check_grid(grid)
        if has_bingo:
            # only check bingo for remaining grid
            boards.remove(grid)
            # if we just finish the last grid return the result !
            if len(boards) == 0:
                total = grid_sum(grid)
                #print(number)
                #print(total)
                print(f'result: {number * total}')
                exit(0)
