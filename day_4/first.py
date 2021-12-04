#!/usr/bin/env python3

BOARD_SIZE=5
#FILE='test.txt' # sol = 188*24=4512
FILE='input.txt' # sol: 394*3701=1458194

number_list = []
bingo_grids = []

def remove_number(nb):
    for grid in range(len(bingo_grids)):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if bingo_grids[grid][row][col] == nb:
                    bingo_grids[grid][row][col] = -1


def check_bingo():
    for grid in range(len(bingo_grids)):
        #print(f'check grid: {grid}')
        # check horizontal
        for row in range(BOARD_SIZE):
            found = True
            for col in range(BOARD_SIZE):
                value = bingo_grids[grid][row][col]
                #print(f'check value[{row},{col}]: {value}')
                if value != -1:
                    found = False
                    break
            if found:
                return [found, grid]
        # check vertical
        for col in range(BOARD_SIZE):
            found = True
            for row in range(BOARD_SIZE):
                value = bingo_grids[grid][row][col]
                #print(f'check value[{row},{col}]: {value}')
                if value != -1:
                    found = False
                    break
            if found:
                return [found, grid]
    return [False, -1]


def get_unmarked_sum(grid_idx):
    grid = bingo_grids[grid_idx]
    grid_sum = 0
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if grid[row][col] != -1:
                grid_sum += grid[row][col]
    return grid_sum


with open(FILE, 'r') as f:
    number_list = [int(i) for i in f.readline().rstrip().split(',')]
    #print(f'numbers: {number_list}')

    grid = []
    row=0
    for line in f:
        line = line.rstrip()
        #print(f'line: {line}')
        if line == '':
            #print('empty')
            continue
        tmp = [int(i) for i in line.split()]
        assert len(tmp) == BOARD_SIZE
        grid.append(tmp)
        row += 1
        if row == BOARD_SIZE:
            row = 0
            bingo_grids.append(grid)
            grid = []
    #print(f'bingo {bingo_grids}')


total = 0
val = 0
for number in number_list:
    #print(f'number: {number}')
    remove_number(number)
    res = check_bingo()

    if res[0]:
        total = get_unmarked_sum(res[1])
        val = number
        break

print(f'result: {total * val}')
#print(f'bingo {bingo_grids}')
