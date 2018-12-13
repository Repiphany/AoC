#!/usr/bin/env python3

import collections
import itertools

class Pots:
    def __init__(self, initial, rules):
        # state stores all values that currently have a plant
        self.state = set(i for i, v in enumerate(initial) if v == '#')
        # store rules that cause a plant to grow
        self.rules = set(rules)
        self.generation = 0

    def next(self, n = None):
        if n is not None:
            for _ in range(n):
                self.next()
            return
        children = set()
        for i in set(itertools.chain(*(range(j - 2, j + 3) for j in self.state))):
            rule = ''.join(self.get_plant(k) for k in range(i - 2, i + 3))
            if rule in self.rules:
                children.add(i)
        self.state = children
        self.generation += 1

    def stabilize(self):
        s = self.string()[0]
        while True:
            self.next()
            s_n = self.string()[0]
            if s == s_n:
                break
            s = s_n

    def get_plant(self, i):
        return '#' if i in self.state else '.'

    def pot_sum(self):
        return sum(self.state)

    def string(self):
        s = ''.join(self.get_plant(i)
                for i in range(min(self.state), max(self.state) + 1))
        return s, min(self.state)

if __name__ == '__main__':
    with open('input', 'r') as f:
        initial = f.readline().strip().split(': ')[-1]
        # skip empty line
        f.readline()
        rules = []
        for line in f:
            rule, out = line.strip().split(' => ')
            if out == '#':
                rules.append(rule)
    pots = Pots(initial, rules)

    # part 1

    pots.next(20)
    print(pots.pot_sum())

    # part 2

    pots.stabilize()

    y1 = pots.pot_sum()
    pots.next()
    y2 = pots.pot_sum()
    m = y2 - y1
    f = lambda x : m*(x - pots.generation) + y2
    print(int(f(50e9)))
    
