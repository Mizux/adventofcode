#!/usr/bin/env python3
FILE='test.txt' # sol: O
FILE='input.txt' # sol: RCPLAKHL

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


def print_fold(dots):
    max_x = 0
    max_y = 0
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]
        if dot[1] > max_y:
            max_y = dot[1]
    for i in range(max_y+1):
        row = ''
        for j in range(max_x+1):
            if (j, i) in dots:
                row += '#'
            else:
                row += ' '
        print(row)


dots, recipe = parse_input(FILE)
#print(f'dots({len(dots)}): {dots}')
#print(f'recipe: {recipe}')
for i in range(len(recipe)):
    axis, pos = recipe.pop(0)
    dots = fold(dots, axis, pos)
    #print(f'dots({len(dots)}): {dots}')
print_fold(dots)
