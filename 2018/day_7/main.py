#!/usr/bin/env python3

import collections

def part_1(restrictions):
    incomplete = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    completed_steps = []
    while len(completed_steps) < 26:
        s_n = sorted([i for i in incomplete
            if len(restrictions[i] - set(completed_steps)) == 0])[0]
        incomplete.discard(s_n)
        completed_steps.append(s_n)
    print(''.join(completed_steps))

if __name__ == '__main__':
    restrictions = collections.defaultdict(set)
    with open('input', 'r') as f:
        for line in f:
            restrictions[line[36]].add(line[5])
    part_1(restrictions)

