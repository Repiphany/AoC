#!/usr/bin/env python3

from .input import get_input
from IPython.terminal.embed import InteractiveShellEmbed
from collections import deque
from itertools import combinations
from functools import lru_cache
from sys import stdin

class XMAS:
    def __init__(self, lines):
        self.numbers = [int(l) for l in lines]

    @lru_cache
    def valid(self, idx, N = 25):
        if idx < N:
            return True
        for a, b in combinations(self.numbers[idx - N:idx], 2):
            if a + b == self.numbers[idx]:
                return True
        return False

    @lru_cache
    def find_invalid(self, N = 25):
        for i, v in enumerate(self.numbers):
            if not self.valid(i, N):
                return v

    @lru_cache
    def weakness(self, N = 25):
        n = self.find_invalid(N = N)
        d = deque([self.numbers[0]])
        for v in self.numbers[1:]:
            while sum(d) > n:
                d.popleft()
            if sum(d) == n:
                return min(d) + max(d)
            if sum(d) < n:
                d.append(v)

def test(args):
    xmas = XMAS("35 20 15 25 47 40 62 55 65 95 102 117 150 182 127 219 299 277 309 576".split(' '))
    assert xmas.find_invalid(5) == 127
    assert xmas.weakness(5) == 62
    print('Tests passed')

def main(args):
    xmas = XMAS(get_input(args.YEAR, args.DAY))
    print(xmas.find_invalid())
    print(xmas.weakness())

