#!/usr/bin/env python3

FILE='test.txt' # sol: 61229
FILE='input.txt' # sol: 1073431

def parse_input(file):
    out = [];
    with open(file, 'r') as f:
        for line in f:
            line = line.rstrip().split(' | ')

            digits = line[0].split(' ')
            # sort segments
            digits = [''.join(sorted(s)) for s in digits]
            assert len(digits) == 10
            #print(f'digit: {digits}')

            output = line[1].split(' ')
            # sort segments
            output = [''.join(sorted(s)) for s in output]
            assert len(output) == 4
            #print(f'output: {output}')

            out.append({'digits': digits, 'output':output})
    #print(f'parsing: {out}')
    return out


def get_digit_with_n_segments(digits, n):
    out = [d for d in digits if len(d) == n]
    #print(f'digits: {out}')
    return out


def find_mapping(digits):
    # find 1, 4, 7, 8
    one = get_digit_with_n_segments(digits, 2)[0]
    four = get_digit_with_n_segments(digits, 4)[0]
    seven = get_digit_with_n_segments(digits, 3)[0]
    eight = get_digit_with_n_segments(digits, 7)[0]
    # find 3 which has all segments of 1 (contrary to 2 and 5)
    three = ''
    l_5 = get_digit_with_n_segments(digits, 5) # [2, 3, 5]
    #print(f'list 5 segments: {l_5}')
    for c in l_5:
        if all(s in c for s in one):
            three = c
            break
    # find 9 which has all segments of 4 (contrary to 0 and 6)
    nine = ''
    l_6 = get_digit_with_n_segments(digits, 6) # [0, 6, 9]
    #print(f'list 6 segments: {l_6}')
    for c in l_6:
        if all(s in c for s in four):
            nine = c
            break
    # between 0 and 6 only 0 contains all segments of 1
    zero = ''
    six = ''
    l_6.remove(nine) # [0, 6]
    for c in l_6:
        if all(s in c for s in one):
            zero = c
            break
    l_6.remove(zero) # [6]
    six = l_6[0]
    # all segments of 5 are in 6 contrary to 2
    two = ''
    five = ''
    l_5.remove(three) # [2, 5]
    #print(f'list 5 segments: {l_5}')
    for c in l_5:
        if all(s in six for s in c):
            five = c
            break
    l_5.remove(five) # [2]
    two = l_5[0]
    #####
    return {
            zero: '0',
            one: '1',
            two: '2',
            three: '3',
            four: '4',
            five: '5',
            six: '6',
            seven: '7',
            eight: '8',
            nine: '9',
            }


def get_code(mapping, output):
    out = ''
    for d in output:
        out += mapping[d]
    return int(out)


entry = parse_input(FILE)
count = 0
for data in entry:
    digits = data['digits']
    output = data['output']
    #print(f'digits: {digits}, output:{output}')

    mapping = find_mapping(digits)
    #print(f'mapping: {mapping}')
    code = get_code(mapping, output)
    print(f'code: {code}')
    count += code
print(f'result: {count}')
