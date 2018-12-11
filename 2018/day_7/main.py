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

def part_2(restrictions, n_workers = 5):
    work_remaining = {l:60+i
            for i, l in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', start = 1)}
    completed_steps = []
    i = 0
    while len(completed_steps) < 26:
        incomplete = set(i for i, v in work_remaining.items() if v)
        s_n = sorted([i for i in incomplete
            if len(restrictions[i] - set(completed_steps)) == 0])[:n_workers]
        for s in s_n:
            work_remaining[s] -= 1
            if not work_remaining[s]:
                completed_steps.append(s)
        i += 1
    print(i)

if __name__ == '__main__':
    restrictions = collections.defaultdict(set)
    with open('input', 'r') as f:
        for line in f:
            restrictions[line[36]].add(line[5])
    part_1(restrictions)
    part_2(restrictions)

