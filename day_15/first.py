#!/usr/bin/env python3
from collections import deque

FILE='test.txt' # sol: 40
FILE='input.txt' # sol: 824

def parse_input(file):
    board = []
    with open(file, 'r') as f:
        for line in f:
            board.append([int(c) for c in line.strip()])
    #print(f'board: {board}')
    return board


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


board = parse_input(FILE)
distance = dijkstra(board, (0,0))
end = (len(board)-1, len(board[0])-1)
print(f'result {distance[end]}')
