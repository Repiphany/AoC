#!/usr/bin/env python3

import collections
import itertools

def part_1(ids):
    twins = triplets = 0
    for i in ids:
        letter_count = collections.Counter(i)
        if 2 in letter_count.values():
            twins += 1
        if 3 in letter_count.values():
            triplets += 1
    print(twins*triplets)

def string_match(s1, s2):
    matching = []
    for l1, l2 in zip(s1, s2):
        if l1 == l2:
            matching.append(l1)
    return ''.join(matching), len(s1) - len(matching)

def part_2(ids):
    for a, b in itertools.combinations(ids, 2):
        matching, dl = string_match(a, b)
        if dl == 1:
            print(matching)
            return

if __name__ == '__main__':
    with open('input', 'r') as f:
        ids = [line.strip() for line in f]
    part_1(ids)
    part_2(ids)

