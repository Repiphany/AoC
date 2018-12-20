#!/usr/bin/env python3

import collections

if __name__ == '__main__':
    known = collections.defaultdict(set)
    min_steps = collections.defaultdict(lambda : float('inf'))
    branches = {}
    cache = []
    def step(steps):
        branch = n = 0
        branched = False
        x, y = (0, 0)
        while True:
            if branched:
                x, y, n = branches[branch]
                branched = False
            n = min_steps[(x, y)] = min(min_steps[(x, y)], n)

            if cache:
                c = cache.pop()
            else:
                c = next(steps)
            if c == '$':
                return
            if c == '(':
                branch += 1
                branches[branch] = (x, y, n)
                continue
            if c == ')':
                branch -= 1
                continue
            if c == '|':
                cn = next(steps)
                if cn == ')':
                    branch -= 1
                    continue
                else:
                    cache.append(cn)
                branched = True
                continue
            if c == 'N':
                y += 1
            if c == 'E':
                x += 1
            if c == 'S':
                y -= 1
            if c == 'W':
                x -= 1
            n += 1
    
    with open('input', 'r') as f:
        step(iter(f.read()))
    print(max(min_steps.items(), key = lambda x : x[1])[1])
    print(len([k for k, v in min_steps.items() if v >= 1000]))
