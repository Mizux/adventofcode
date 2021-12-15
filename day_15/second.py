#!/usr/bin/env python3
from collections import deque

FILE='test.txt' # sol: 40
FILE='input.txt' # sol: 824

def print_board(board):
    for row in board:
        print(''.join([str(i) for i in row]))


def parse_input(file, repeat):
    board = []
    for i in range(repeat):
      with open(file, 'r') as f:
          for line in f:
              board.append([int(c) for c in line.strip()] * repeat)
    #print_board(board)
    return board


def compute_board(board, repeat):
    height = len(board) // repeat
    width = len(board[0]) // repeat
    # for each grid row
    for row_repeat in range(repeat):
        if row_repeat != 0: # don't touch grid (0,0)
            # update first grid column
            for row in range(height):
                for col in range(width):
                    if board[height*(row_repeat-1)+row][col] < 9:
                        board[height*row_repeat+row][col] = board[height*(row_repeat-1)+row][col] + 1
                    else:
                        board[height*row_repeat+row][col] = 1
        # update remaining grid columns
        for col_repeat in range(1, repeat):
            for row in range(height):
                for col in range(width):
                    if board[height*row_repeat+row][width*(col_repeat-1)+col] < 9:
                        board[height*row_repeat+row][width*col_repeat+col] = board[height*row_repeat+row][width*(col_repeat-1)+col] + 1
                    else:
                        board[height*row_repeat+row][width*col_repeat+col] = 1


def get_neighbour(board, pos):
    out = []
    if pos[0] > 0:
        out.append((pos[0]-1, pos[1]))
    if pos[0] < len(board) - 1:
        out.append((pos[0]+1, pos[1]))
    if pos[1] > 0:
        out.append((pos[0], pos[1] - 1))
    if pos[1] < len(board[0]) - 1:
        out.append((pos[0], pos[1] + 1))
    return out


def dijkstra(board, start):
    queue = deque([start])
    distance = {start: 0}
    while queue:
        cur = queue.popleft()
        for point in get_neighbour(board, cur):
                dst = distance[cur] + board[point[0]][point[1]]
                if (point not in distance or dst < distance[point]):
                    distance[point] = dst
                    queue.append(point)
    return distance


repeat = 5
board = parse_input(FILE, repeat)
#print('in:')
#print_board(board)
compute_board(board, repeat)
#print('out:')
#print_board(board)

distance = dijkstra(board, (0,0))
end = (len(board)-1, len(board[0])-1)
print(f'result {distance[end]}')
