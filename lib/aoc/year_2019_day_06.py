#!/usr/bin/env python3

from .input import get_input
from collections import defaultdict

class Orbit:
    def __init__(self, name = None):
        self.name = name
        self.parent = None
        self.direct = set()

    def __repr__(self):
        return f'<Orbit: {self.name}>'

    def indirect(self, objects):
        s = 0
        for o in self.direct:
            s += len(o.direct) + o.indirect(objects)
        return s
    
    def tree(self):
        p = self.parent
        while p is not None:
            yield p
            p = p.parent

def test(args):
    print('Tests passed')

def main(args):
    objects = defaultdict(Orbit)
    for line in get_input(args.YEAR, args.DAY):
        a, b = line.strip().split(')')
        objects[a].name = a
        objects[b].name = b
        objects[a].direct.add(objects[b])
        objects[b].parent = objects[a]
    direct = sum(len(o.direct) for o in objects.values())
    indirect = sum(o.indirect(objects) for o in objects.values())
    print(direct + indirect)
    you_tree = list(objects['YOU'].tree())
    san_tree = list(objects['SAN'].tree())
    closest = min(set(you_tree).intersection(set(san_tree)), key = san_tree.index)
    print(you_tree.index(closest) + san_tree.index(closest))

