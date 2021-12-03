#!/usr/bin/env python3

#FILE = 'test.txt' # sol 23*10:230
#WORD_SIZE=5
FILE = 'input.txt' # sol 789*3586:2829354
WORD_SIZE=12

def filter_number(input_list, bit_pos, bit_value):
    '''filter out a list of number'''
    assert bit_pos in range(WORD_SIZE)
    assert bit_value in [0,1]
    output = []
    for number in input_list:
        mask = 0x1
        if (number >> bit_pos) & mask == bit_value:
            output.append(number)
    #print(f'filtered list size: {len(output)}')
    return output


def get_most_common_bit(input_list, bit_pos):
    '''Get most significant bit
    return 1, 0 or -1 (if equals)
    '''
    assert bit_pos in range(WORD_SIZE)
    counter = 0
    mask = 0x1 << i
    for number in input_list:
        if number & mask:
            counter += 1
        else:
            counter -= 1
    if counter > 0:
        return 1
    elif counter == 0:
        return -1
    else:
        return 0


def get_least_common_bit(input_list, bit_pos):
    bit = get_most_common_bit(input_list, bit_pos)
    if bit == 1:
        bit = 0
    elif bit == 0:
        bit = 1
    return bit


with open(FILE, 'r') as f:
    input_list = []
    for line in f:
        input_list.append(int(line, base=2))

    # Find oxygen
    oxygen = 0
    filter_list = input_list.copy()
    for i in reversed(range(WORD_SIZE)):
        bit = get_most_common_bit(filter_list, i)
        if bit == -1: # in case of tie use 1
            bit = 1
        #print(f'bit: {bit}')
        filter_list = filter_number(filter_list, i, bit)
        if len(filter_list) == 1:
            oxygen = filter_list[0]
            break
    print(f'oxygen: {oxygen}')

    # Find oxygen
    co2 = 0
    filter_list = input_list.copy()
    for i in reversed(range(WORD_SIZE)):
        bit = get_least_common_bit(filter_list, i)
        if bit == -1: # in case of tie use 0
            bit = 0
        #print(f'bit: {bit}')
        filter_list = filter_number(filter_list, i, bit)
        if len(filter_list) == 1:
            co2 = filter_list[0]
            break
    print(f'co2: {co2}')

print(f'result: {oxygen * co2}')
