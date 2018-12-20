#!/usr/bin/env python3

import collections

class Facility:
    def __init__(self):
        self.min_steps = collections.defaultdict(lambda : float('inf'))

    def step(self, directions):
        branches = {}
        branch = n = x = y = 0
        branched = False
        while True:
            if branched:
                x, y, n = branches[branch]
                branched = False
            n = self.min_steps[(x, y)] = min(self.min_steps[(x, y)], n)
            c = next(directions)
            if c == '$':
                return
            if c == '(':
                branch += 1
                branches[branch] = (x, y, n)
            if c == ')':
                branch -= 1
            if c == '|':
                branched = True
            if c == 'N':
                y += 1
            if c == 'S':
                y -= 1
            if c == 'E':
                x += 1
            if c == 'W':
                x -= 1
            n += 1

if __name__ == '__main__':
    facility = Facility()
    with open('input', 'r') as f:
        facility.step(iter(f.read()))
    print(max(facility.min_steps.items(), key = lambda x : x[1])[1])
    print(len([k for k, v in facility.min_steps.items() if v >= 1000]))
