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

    def next(self):
        children = set()
        for i in set(itertools.chain(*(range(j - 2, j + 3) for j in self.state))):
            rule = ''.join(self.get_plant(k) for k in range(i - 2, i + 3))
            if rule in self.rules:
                children.add(i)
        self.state = children
        self.generation += 1

    def get_plant(self, i):
        return '#' if i in self.state else '.'

    def pot_sum(self):
        return sum(self.state)

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
    for _ in range(20):
        pots.next()
    print(pots.pot_sum())

    # part 2
    # wait for plant population to stabilize

    population = []
    for _ in range(5):
        pots.next()
        population.append(len(pots.state))

    while True:
        if len(set(population[-5:])) == 1:
            break
        pots.next()
        population.append(len(pots.state))

    y1 = pots.pot_sum()
    pots.next()
    y2 = pots.pot_sum()
    m = y2 - y1
    f = lambda x : m*(x - pots.generation) + y2
    print(int(f(50e9)))
    
