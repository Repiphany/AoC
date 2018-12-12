#!/usr/bin/env python3

import collections

class Pots:
    def __init__(self, initial):
        self.state = collections.defaultdict(lambda : '.')
        for i, x in enumerate(initial):
            self.state[i] = x
        self.rules = collections.defaultdict(lambda : '.')
        self.generation = 0

    def next(self):
        changes = []
        for i in range(min(self.state.keys()) - 3, max(self.state.keys()) + 3):
            r = ''.join(self.state[j] for j in range(i - 2, i + 3))
            changes.append((i, self.rules[r]))
        for i, o in changes:
            self.state[i] = o
        # clear pots that are empty from state
        for k, v in list(self.state.items()):
            if v == '.':
                del self.state[k]
        self.generation += 1

    def pot_sum(self):
        return sum(k for k, v in self.state.items() if v == '#')


if __name__ == '__main__':
    with open('input', 'r') as f:
        initial = f.readline().strip().split(': ')[-1]
        pots = Pots(initial)
        f.readline()
        for line in f:
            rule, out = line.strip().split(' => ')
            pots.rules[rule] = out
    # part 1
    for _ in range(20):
        pots.next()
    print(pots.pot_sum())

    # part 2

    # pot sum growth stabilizes after many generations (>150)
    for _ in range(180):
        pots.next()
    y_200 = pots.pot_sum()
    pots.next()
    y_201 = pots.pot_sum()
    m = y_201 - y_200
    f = lambda x : m*(x - 200)+y_200
    print(int(f(50e9)))
    
