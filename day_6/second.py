#!/usr/bin/env python3

FILE='test.txt' # sol: 256=26984457539
FILE='input.txt' # sol: 256:1572643095893

def parse_input(file):
    with open(file, 'r') as f:
        k = f.readline().rstrip()
        print(f'initial state: {k}')
        numbers = [int(i) for i in k.split(',')]
        population = [0] * 9
        for n in numbers:
            population[n] += 1
    print(f'population: {population}')
    return population


def grow(population):
    out = [0] * 9
    for i in range(8):
        out[i] = population[i+1]

    out[6] += population[0]
    out[8] = population[0]
    print(f'population: {out}')
    return out


pop = parse_input(FILE)
for i in range(256):
    pop = grow(pop)
print(f'result {sum(pop)}')
