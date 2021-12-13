#!/usr/bin/env python3
FILE='test.txt' # sol: 17
FILE='input.txt' # sol: 743

def parse_input(file):
    with open(file, 'r') as f:
        coordinates, instructions = f.read().split('\n\n')
        #print(f'coordinate:\n{coordinates}')
        #print(f'instructions:\n{instructions}')

    # parse dots
    dots = set()
    for line in coordinates.split('\n'):
        dots.add(tuple([int(i) for i in line.split(',')]))
    #print(dots)

    # Parse instruction
    recipe = []
    for line in instructions.rstrip().split('\n'):
        axis, pos = line.replace('fold along ','').split('=')
        pos = int(pos)
        recipe.append((axis, pos))
    #print(recipe)

    return dots, recipe


def fold(dots, axis, pos):
    new_dots = set()
    for dot in dots:
        #print(f'dot: {dot}')
        if axis == 'x' and dot[0] > pos:
            folded = (pos - (dot[0]-pos), dot[1])
            #print(f'folded: {folded}')
            new_dots.add(folded)
        elif axis == 'y' and dot[1] > pos:
            folded = (dot[0], pos - (dot[1]-pos))
            #print(f'folded: {folded}')
            new_dots.add(folded)
        else:
            #print(f'not folded: {dot}')
            new_dots.add(dot)
    return new_dots


dots, recipe = parse_input(FILE)
#print(f'dots({len(dots)}): {dots}')
#print(f'recipe: {recipe}')
for i in range(1):
    axis, pos = recipe.pop(0)
    dots = fold(dots, axis, pos)
    #print(f'dots({len(dots)}): {dots}')
print(f'result {len(dots)}')
