#!/usr/bin/env python3

from .input import get_input
from functools import lru_cache
from collections import defaultdict

class Containers:
    def __init__(self, lines):
        self.rules = defaultdict(dict)
        self.bags = set()
        for line in lines:
            line = line.strip('.\n')
            container, contain = line.split(' contain ')
            container = container.replace('bags', 'bag')
            self.bags.add(container)
            for rule in contain.split(', '):
                try:
                    n, c = rule.split(' ', maxsplit = 1)
                    c = c.replace('bags', 'bag')
                    self.rules[container][c] = int(n)
                    self.bags.add(c)
                except:
                    pass

    @lru_cache(maxsize = None)
    def search_outer(self, container, target):
        if target in self.rules[container]:
            return True
        else:
            return any(self.search_outer(c, target) for c in self.rules[container])

    @lru_cache(maxsize = None)
    def contains(self, bag):
        return sum(m + m*self.contains(bi) for bi, m in self.rules[bag].items())

    def count_outermost(self, target):
        return sum(self.search_outer(b, target) for b in self.bags)
     
def test(args):
    print('Tests passed')

def main(args):
    containers = Containers(get_input(args.YEAR, args.DAY))
    print(containers.count_outermost('shiny gold bag'))
    print(containers.contains('shiny gold bag'))

