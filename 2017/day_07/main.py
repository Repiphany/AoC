#!/usr/bin/env python3

import argparse
import re

class Tower:
    programs = {}
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self._children = children
        self._parent = None

    def __repr__(self):
        return '<Tower: {} ({}) ({})>'.format(self.name, self.weight, self._children)

    @property
    def children(self):
        return [Tower.programs[prog] for prog in self._children]

    @property
    def parent(self):
        if self._parent is not None:
            return self._parent
        for prog in Tower.programs.values():
            if self in prog.children:
                self._parent = prog
                return prog
        self._parent = ''
        return self._parent

    @property
    def total_weight(self):
        return self.weight + sum(c.total_weight for c in self.children)

    @property
    def siblings(self):
        if self.parent:
            return [c for c in self.parent.children if c is not self]
        return []

    @property
    def sibling_weights(self):
        return set([s.total_weight for s in self.siblings])

    @property
    def balanced(self):
        return len(set([c.total_weight for c in self.children])) == 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            name = line.split(' ')[0]
            weight = int(line.split(' ')[1][1:-1])
            try:
                children = line.split('-> ')[1].split(', ')
            except IndexError:
                children = []
            tower = Tower(name, weight, children)
            Tower.programs[name] = tower
    for name, prog in Tower.programs.items():
        if not prog.parent:
            print(name)

    unbalanced = [p for p in Tower.programs.values()
            if p.balanced and len(p.sibling_weights) == 1
            and all(len(s.sibling_weights) == 2 for s in p.siblings)][0]
    good_weight, = unbalanced.sibling_weights
    print(unbalanced.weight + good_weight - unbalanced.total_weight)
