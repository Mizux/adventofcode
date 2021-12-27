#!/usr/bin/env python3.10
from collections import defaultdict

FILE = 'test.txt'  # sol: 3621
FILE='input.txt' # sol: 10707

def parse_input(file):
    scanners = []
    with open(file, 'r') as f:
        scanner_reports = f.read().strip().split('\n\n')
        for report in scanner_reports:
            beacons = []
            #print(f'report: {report}')
            for line in report.split('\n'):
                if '--' in line:
                    continue
                coordinates = tuple(int(c) for c in line.split(','))
                beacons.append(coordinates)
            #print(f'beacons: {beacons}')
            scanners.append(beacons)
    #print(f'scanners: {scanners}')
    return scanners


def rotate_point(p, rotation):
    x, y, z = p
    match rotation:
      case 0:
        return (x, y, z)
      case 1:
        return (x, -z, y)
      case 2:
        return (x, -y, -z)
      case 3:
        return (x, z, -y)
      case 4:
        return (-x, -y, z)
      case 5:
        return (-x, -z, -y)
      case 6:
        return (-x, y, -z)
      case 7:
        return (-x, z, y)
      case 8:
        return (y, x, -z)
      case 9:
        return (y, -x, z)
      case 10:
        return (y, z, x)
      case 11:
        return (y, -z, -x)
      case 12:
        return (-y, x, z)
      case 13:
        return (-y, -x, -z)
      case 14:
        return (-y, -z, x)
      case 15:
        return (-y, z, -x)
      case 16:
        return (z, x, y)
      case 17:
        return (z, -x, -y)
      case 18:
        return (z, -y, x)
      case 19:
        return (z, y, -x)
      case 20:
        return (-z, x, -y)
      case 21:
        return (-z, -x, y)
      case 22:
        return (-z, y, x)
      case 23:
        return (-z, -y, -x)
      case _:
        print(f'rotation {rotation} unknow!')
        exit(2)


def add_points(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 + x2, y1 + y2, z1 + z2)


def subtract_points(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2, y1 - y2, z1 - z2)


def invert_point(p):
    x, y, z = p
    return (-x, -y, -z)


def manhattan_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)


# Main
scanners = parse_input(FILE)
beacons = set(scanners.pop(0))
scanner_coords = []
while scanners:
    scanner = scanners.pop(0)
    match = False
    for rotation in range(24):
        offsets = defaultdict(int)
        for beacon in beacons:
            for point in scanner:
                rotated_point = rotate_point(point, rotation)
                offset = subtract_points(rotated_point, beacon)
                offsets[offset] += 1
        for offset, count in offsets.items():
            if count >= 12:
                match = True
                scanner_coord = invert_point(offset)
                scanner_coords.append(scanner_coord)
                for point in scanner:
                    point = rotate_point(point, rotation)
                    beacons.add(add_points(point, scanner_coord))
        continue
    if not match:
        scanners.append(scanner)

scanner_distances = 0
for i, p1 in enumerate(scanner_coords):
    for p2 in scanner_coords[i+1:]:
        scanner_distances = max(scanner_distances, manhattan_distance(p1, p2))
print(f"result: {scanner_distances}")
