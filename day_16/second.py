#!/usr/bin/env python3.10
FILE='test_s1.txt' # in: C200B40A82 sol: 3
FILE='test_s2.txt' # in: 04005AC33890 sol: 54
FILE='test_s3.txt' # in: 880086C3E88112 sol: 7
FILE='test_s4.txt' # in: CE00C43D881120 sol: 9
FILE='test_s5.txt' # in: D8005AC2A8F0 sol: 1
FILE='test_s6.txt' # in: F600BC2D8F sol: 0
FILE='test_s7.txt' # in: 9C005AC2F8F0 sol: 0
FILE='test_s8.txt' # in: 9C0141080250320F1802104A08 sol: 1

FILE='input.txt' # sol: 1549026293044


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
    print(' ' * level + f'parsing packet...')
    #print(' ' * level + f'parsing packet: {binary}')

    version = int(binary[0:3],2)
    #print(' ' * level + f'version: {version}')
    binary = binary[3:]

    type_id = int(binary[0:3],2)
    #print(' ' * level + f'type_id: {type_id}')
    binary = binary[3:]

    number = 0
    match type_id:
        case 0:
            number, binary = parse_sum(binary, level)
        case 1:
            number, binary = parse_product(binary, level)
        case 2:
            number, binary = parse_minimum(binary, level)
        case 3:
            number, binary = parse_maximum(binary, level)
        case 4:
            number, binary = parse_number(binary, level)
        case 5:
            number, binary = parse_greater_than(binary, level)
        case 6:
            number, binary = parse_less_than(binary, level)
        case 7:
            number, binary = parse_equal_to(binary, level)
        case 8:
            number, binary = parse_operators(binary, level)
        case _:
            print('unsupported')
            assert False
    return number, binary


def parse_sum(binary, level):
    print(' ' * level + 'parsing sum...')
    total = 0
    length_type_id = int(binary[0])
    binary = binary[1:]
    if length_type_id == 0:
        length_subpacket = int(binary[0:15], 2)
        binary = binary[15:]
        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            number, sub_binary = parse_packet(sub_binary, level+1)
            total += number
    elif length_type_id == 1:
        nb_subpacket = int(binary[0:11], 2)
        binary = binary[11:]
        for i in range(nb_subpacket):
            number, binary = parse_packet(binary, level+1)
            total += number
    print(' ' * level + f'sum: {total}')
    return total, binary


def parse_product(binary, level):
    print(' ' * level + f'parsing product...')
    total = 1
    length_type_id = int(binary[0])
    binary = binary[1:]
    if length_type_id == 0:
        length_subpacket = int(binary[0:15], 2)
        binary = binary[15:]
        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            number, sub_binary = parse_packet(sub_binary, level+1)
            total *= number
    elif length_type_id == 1:
        nb_subpacket = int(binary[0:11], 2)
        binary = binary[11:]
        for i in range(nb_subpacket):
            number, binary = parse_packet(binary, level+1)
            total *= number
    print(' ' * level + f'product: {total}')
    return total, binary


def parse_minimum(binary, level):
    print(' ' * level + f'parsing minimum...')
    minimum = None
    length_type_id = int(binary[0])
    binary = binary[1:]
    if length_type_id == 0:
        length_subpacket = int(binary[0:15], 2)
        binary = binary[15:]
        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            number, sub_binary = parse_packet(sub_binary, level+1)
            if minimum == None or number < minimum:
                minimum = number
    elif length_type_id == 1:
        nb_subpacket = int(binary[0:11], 2)
        binary = binary[11:]
        for i in range(nb_subpacket):
            number, binary = parse_packet(binary, level+1)
            if minimum == None or number < minimum:
                minimum = number
    print(' ' * level + f'minimum: {minimum}')
    return minimum, binary


def parse_maximum(binary, level):
    print(' ' * level + f'parsing maximum...')
    maximum = None
    length_type_id = int(binary[0])
    binary = binary[1:]
    if length_type_id == 0:
        length_subpacket = int(binary[0:15], 2)
        binary = binary[15:]
        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            number, sub_binary = parse_packet(sub_binary, level+1)
            if maximum == None or number > maximum:
                maximum = number
    elif length_type_id == 1:
        nb_subpacket = int(binary[0:11], 2)
        binary = binary[11:]
        for i in range(nb_subpacket):
            number, binary = parse_packet(binary, level+1)
            if maximum == None or number > maximum:
                maximum = number
    print(' ' * level + f'maximum: {maximum}')
    return maximum, binary


def parse_number(binary, level):
    print(' ' * level + f'parsing number...')
    number = ''
    has_next = 1
    # [has_next + 'WXYZ']+
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


def parse_greater_than(binary, level):
    print(' ' * level + f'parsing greater than...')
    a = None
    b = None
    length_type_id = int(binary[0])
    binary = binary[1:]
    if length_type_id == 0:
        length_subpacket = int(binary[0:15], 2)
        binary = binary[15:]
        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            number, sub_binary = parse_packet(sub_binary, level+1)
            if a == None:
                a = number
            elif b == None:
                b = number
            else:
                print('error more than 2 literals')
                assert False
    elif length_type_id == 1:
        nb_subpacket = int(binary[0:11], 2)
        binary = binary[11:]
        assert nb_subpacket == 2
        a, binary = parse_packet(binary, level+1)
        b, binary = parse_packet(binary, level+1)
    assert a != None and b != None
    greater = 1 if a > b else 0
    print(' ' * level + f'greater: {greater}')
    return greater, binary


def parse_less_than(binary, level):
    print(' ' * level + f'parsing less than...')
    a = None
    b = None
    length_type_id = int(binary[0])
    binary = binary[1:]
    if length_type_id == 0:
        length_subpacket = int(binary[0:15], 2)
        binary = binary[15:]
        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            number, sub_binary = parse_packet(sub_binary, level+1)
            if a == None:
                a = number
            elif b == None:
                b = number
            else:
                print('error more than 2 literals')
                assert False
    elif length_type_id == 1:
        nb_subpacket = int(binary[0:11], 2)
        binary = binary[11:]
        assert nb_subpacket == 2
        a, binary = parse_packet(binary, level+1)
        b, binary = parse_packet(binary, level+1)
    assert a != None and b != None
    less = 1 if a < b else 0
    print(' ' * level + f'less: {less}')
    return less, binary


def parse_equal_to(binary, level):
    print(' ' * level + f'parsing equal to...')
    a = None
    b = None
    length_type_id = int(binary[0])
    binary = binary[1:]
    if length_type_id == 0:
        length_subpacket = int(binary[0:15], 2)
        binary = binary[15:]
        sub_binary = binary[0:length_subpacket]
        binary = binary[length_subpacket:]
        while sub_binary:
            number, sub_binary = parse_packet(sub_binary, level+1)
            if a == None:
                a = number
            elif b == None:
                b = number
            else:
                print('error more than 2 literals')
                assert False
    elif length_type_id == 1:
        nb_subpacket = int(binary[0:11], 2)
        binary = binary[11:]
        assert nb_subpacket == 2
        a, binary = parse_packet(binary, level+1)
        b, binary = parse_packet(binary, level+1)
    assert a != None and b != None
    equal = 1 if a == b else 0
    print(' ' * level + f'equal: {equal}')
    return equal, binary


def parse_operators(binary, level):
    print(' ' * level + 'operator 8 is undefined')
    assert False
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
number, binary = parse_packet(binary, 0)
print(f'result: {number}')
