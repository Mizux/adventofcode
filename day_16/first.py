#!/usr/bin/env python3.10
FILE='test_1.txt' # sol: 6
FILE='test_2.txt' # sol: 1
FILE='test_3.txt' # sol: 7

FILE='example_1.txt' # sol: 16
FILE='example_2.txt' # sol: 12
FILE='example_3.txt' # sol: 23
FILE='example_4.txt' # sol: 31

FILE='input.txt' # sol: 963


def parse_input(file):
    with open(file, 'r') as f:
        line = f.readline().rstrip()
        print(f'line: {line}')
        binary = ''
        for c in line:
            match c:
                case '0':
                    binary += '0000'
                case '1':
                    binary += '0001'
                case '2':
                    binary += '0010'
                case '3':
                    binary += '0011'
                case '4':
                    binary += '0100'
                case '5':
                    binary += '0101'
                case '6':
                    binary += '0110'
                case '7':
                    binary += '0111'
                case '8':
                    binary += '1000'
                case '9':
                    binary += '1001'
                case 'A':
                    binary += '1010'
                case 'B':
                    binary += '1011'
                case 'C':
                    binary += '1100'
                case 'D':
                    binary += '1101'
                case 'E':
                    binary += '1110'
                case 'F':
                    binary += '1111'
        #binary = format(int(line, 16), 'b')
    print(f'binary: {binary}')
    return binary


def parse_packet(binary, level):
    print(' ' * level + f'parsing packet: {binary}')

    version = int(binary[0:3],2)
    print(' ' * level + f'version: {version}')
    binary = binary[3:]

    type_id = int(binary[0:3],2)
    print(' ' * level + f'type_id: {type_id}')
    binary = binary[3:]

    if type_id == 4:
        number, binary = parse_number(binary, level)
    else:
        sub_ver, binary = parse_operators(binary, level)
        version += sub_ver
    return version, binary


def parse_number(binary, level):
    print(' ' * level + f'parsing number:...')

    number = ''
    has_next = 1
    while has_next == 1:
        has_next = int(binary[0])
        #print(' ' * level + f'has next: {has_next}')
        binary = binary[1:]

        tmp = binary[0:4]
        #print(' ' * level + f'tmp: {tmp}')
        binary = binary[4:]

        number += tmp
    number = int(number, 2)
    print(' ' * level + f'number: {number}')
    return number, binary


def parse_operators(binary, level):
    version = 0
    length_type_id = int(binary[0])
    print(' ' * level + f'length type id: {length_type_id}')
    binary = binary[1:]
    if length_type_id == 0:
        print(' ' * level + 'parsing 15 bits')
        length_subpacket = int(binary[0:15], 2)
        print(' ' * level + f'length_subpacket: {length_subpacket}')
        binary = binary[15:]

        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            sub_ver, sub_binary = parse_packet(sub_binary, level+1)
            version += sub_ver
            print()
    elif length_type_id == 1:
        print(' ' * level + 'parsing 11 bits')
        nb_subpacket = int(binary[0:11], 2)
        print(' ' * level + f'nb_subpacket: {nb_subpacket}')
        binary = binary[11:]

        for i in range(nb_subpacket):
            sub_ver, binary = parse_packet(binary, level+1)
            print()
            version += sub_ver
    else:
        print(' ' * level + 'parsing error !')
        return
    return version, binary


# Main
binary = parse_input(FILE)
version, _ = parse_packet(binary, 0)
print(f'total version: {version}')
