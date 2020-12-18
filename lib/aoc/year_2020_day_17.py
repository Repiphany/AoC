#!/usr/bin/env python3

from .input import get_input
import collections
import itertools
import functools

class Game:
    def __init__(self, lines):
        self.init = [(x, y) for y, line in enumerate(lines)
                for x, c in enumerate(line) if c == '#']

    def active(self, D):
        return set(i + (0,)*(D - 2) for i in self.init)

    @functools.lru_cache
    def d_neighbours(self, d):
        return tuple(i for i in itertools.product([-1,0,1], repeat = d) if any(i))

    def neighbours(self, pt):
        for n in self.d_neighbours(len(pt)):
            yield tuple(x + i for x, i in zip(pt, n))

    def tick(self, active):
        active_n = collections.defaultdict(int, {pt:0 for pt in active})
        for pt in active:
            for n in self.neighbours(pt):
                active_n[n] += 1
        switch = set(pt for pt, v in active_n.items()
                if (v not in [2,3] and pt in active)
                or (v == 3 and pt not in active))
        active ^= switch

    def run(self, N, D = 3):
        active = self.active(D)
        for i in range(N):
            self.tick(active)
        return len(active)

def test(args):
    game = Game(""".#.
..#
###""".split('\n'))
    assert game.run(6, D = 3) == 112
    assert game.run(6, D = 4) == 848
    print('Tests passed')

def main(args):
    game = Game(get_input(args.YEAR, args.DAY))
    print(game.run(6, D = 3))
    print(game.run(6, D = 4))


