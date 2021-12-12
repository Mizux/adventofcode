#!/usr/bin/env python3
FILE='test_1.txt' # sol: 10
FILE='test_2.txt' # sol: 19
FILE='test_3.txt' # sol: 226
FILE='input.txt' # sol: 5756

def parse_input(file):
    graph = {}
    graph['start'] = []
    graph['end'] = []
    with open(file, 'r') as f:
        for line in f:
            a, b = line.rstrip().split('-')
            #print(f'parsing: {a}-{b} ...')
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]
            if b in graph:
                graph[b].append(a)
            else:
                graph[b] = [a]
    return graph


def extend_paths(paths, node):
    pathsCopy = []
    for p in paths:
        tmp = p.copy()
        tmp.append(node)
        pathsCopy.append(tmp)
    return pathsCopy


def get_paths(graph, current, visited, paths):
    #print(f'current: {current}, paths: {paths}')
    if current == 'end':
        return paths
    out = []
    for next_node in graph[current]:
        #print(''.join([' ']*len(paths[0]))+f'next_node: {next_node}')
        if next_node in visited:
            #print(''.join([' ']*len(paths[0]))+'dead end')
            continue
        if next_node.islower():
            visitedCopy = visited.copy()
            visitedCopy.add(next_node)
            pathsCopy = extend_paths(paths, next_node)
            next_path = get_paths(graph, next_node, visitedCopy, pathsCopy)
            if next_path != []:
                out.extend(next_path)
        else:
            pathsCopy = extend_paths(paths, next_node)
            next_path = get_paths(graph, next_node, visited, pathsCopy)
            if next_path != []:
                out.extend(next_path)
    #print(f'curent:{current} out: {out}')
    return out


graph = parse_input(FILE)
print(f'graph: {graph}')
current = 'start'
visited = {'start'}
paths = get_paths(graph, current, visited, [['start']])
print(f'paths: {paths}')

print(f'result {len(paths)}')
