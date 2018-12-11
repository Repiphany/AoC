#!/usr/bin/env python3

import collections

def part_1(ids):
    twins = triplets = 0
    for i in ids:
        letter_count = collections.Counter(i)
        if 2 in letter_count.values():
            twins += 1
        if 3 in letter_count.values():
            triplets += 1
    print(twins*triplets)

if __name__ == '__main__':
    with open('input', 'r') as f:
        ids = [line.strip() for line in f]
    part_1(ids)

