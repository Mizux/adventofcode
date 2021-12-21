#!/usr/bin/env python3.10
FILE='input.txt' # sol: 4600


def parse_input(file):
    lines = []
    with open(file, 'r') as f:
        for line in f:
            lines.append(line.rstrip())
    #print(f'lines: {lines}')
    return lines


def to_string(n):
    if isinstance(n, int):
        return str(n)
    string = '['
    for i in range(len(n)):
        string += to_string(n[i])
        if i < len(n) - 1:
            string += ','
    string += ']'
    return string


def compute_sum(left, right):
    # Step 1: merge
    nb = left.copy()
    nb.extend(right)
    # Step 2: increase depth
    for i in range(len(nb)):
        nb[i] = (nb[i][0], nb[i][1]+1)
    #print(f'merged: {nb}')
    # Step 3: reduce
    updated = True
    while updated:
       updated , nb = try_explode(nb)
       if updated:
           #print(f'explode: {nb}')
           continue
       updated, nb = try_split(nb)
       if updated:
           #print(f'split: {nb}')
           pass
    return nb


def try_explode(nb):
    exploded = False
    previous = None
    for i in range(len(nb)-1):
        if nb[i][1] == 5 and nb[i+1][1] == 5:
            # add left
            if previous != None:
                nb[previous] = (nb[previous][0] + nb[i][0], nb[previous][1])
            # add right
            if len(nb) > i+2:
                nb[i+2] = (nb[i+2][0] + nb[i+1][0], nb[i+2][1])
            #remove pair
            del nb[i+1]
            nb[i] = (0, nb[i][1]-1)
            exploded = True
            break
        else:
            previous = i;
    return exploded, nb


def try_split(nb):
    for idx, t in enumerate(nb):
        if t[0] >= 10:
            depth = t[1]
            left = t[0] // 2
            right = t[0] - left
            nb[idx] = (left, depth+1)
            nb.insert(idx+1, (right, depth+1))
            return True, nb
    return False, nb


def parse_number(line):
    out = []
    tmp = ''
    depth = 0
    for k in line:
        match k:
          case '[':
            if tmp != '':
                out.append((int(tmp), depth))
                tmp = ''
            depth += 1
          case ']':
            if tmp != '':
                out.append((int(tmp), depth))
                tmp = ''
            depth -= 1
          case ',':
            if tmp != '':
                out.append((int(tmp), depth))
                tmp = ''
          case _:
            tmp += k
    return out


def amplitude(nb):
    if len(nb) == 1:
        return nb[0][0]
    elif len(nb) == 2:
        return 3 * nb[0][0] + 2 * nb[1][0]
    else:
        out = []
        i = 0
        while i < len(nb)-1:
            if nb[i][1] == nb[i+1][1]:
                out.append((3 * nb[i][0] + 2 * nb[i+1][0], nb[i][1] - 1))
                i += 1
            else:
                out.append(nb[i])
            i += 1
        if nb[-1][1] != nb[-2][1]:
            out.append(nb[-1])

        if len(out) == len(nb):
            return 3 * nb[0][0] + 2 * amplitude(out[1:])
        else:
            return amplitude(out)


# Main
lines = parse_input(FILE)

max_amplitude = 0
for i in range(len(lines)):
  for j in range(len(lines)):
      if i == j:
          continue
      print(f'amplitude for {i},{j}')
      nb = compute_sum(parse_number(lines[i]), parse_number(lines[j]))
      print(f'sum {nb}')
      value = amplitude(nb)
      print(f'amplitude {value}')
      max_amplitude = max(max_amplitude, value)
print(f'result: {max_amplitude}')
