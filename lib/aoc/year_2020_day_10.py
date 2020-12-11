#!/usr/bin/env python3

from .input import get_input
from collections import Counter
from functools import lru_cache

class Adapters:
    def __init__(self, lines):
        self.adapters = sorted([int(i) for i in lines])

    def chain(self):
        return [b - a for a, b in zip([0] + self.adapters, self.adapters)] + [3]

    def joltage_differences(self):
        return Counter(self.chain())

    @lru_cache(maxsize = None)
    def count_arrangements(self, v):
        if v and v not in self.adapters:
            return 0
        if v == max(self.adapters):
            return 1
        branches = sum(self.count_arrangements(j) for j in [v+1, v+2, v+3])
        return branches

    def reverse_count(self):
        for v in reversed(self.adapters):
            self.count_arrangements(v)
        return self.count_arrangements(0)

def test(args):
    adapters = Adapters("16 10 15 5 1 11 7 19 6 12 4".split(' '))
    jd = adapters.joltage_differences()
    assert jd[1] == 7
    assert jd[3] == 5
    assert adapters.reverse_count() == 8

    adapters = Adapters("28 33 18 42 31 14 46 20 48 47 24 23 49 45 19 38 39 11 1 32 25 35 8 17 7 9 4 2 34 10 3".split(' '))
    jd = adapters.joltage_differences()
    assert jd[1] == 22
    assert jd[3] == 10
    assert adapters.reverse_count() == 19208

    print('Tests passed')

def main(args):
    adapters = Adapters(get_input(args.YEAR, args.DAY))
    jd = adapters.joltage_differences()
    print(jd[1]*jd[3])
    print(adapters.reverse_count())

