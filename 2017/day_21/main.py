#!/usr/bin/env python3

import argparse
import collections
import numpy as np
import sys

def pattern_equivalent(s, rules):
    if len(s) == 4:
        g = np.asarray(list(s)).reshape((2,2))
    else:
        g = np.asarray(list(s)).reshape((3,3))
    for f in range(2):
        for r in range(4):
            g = np.rot90(g)
            gs = ''.join(g.flatten())
            if gs in rules.keys():
                return gs
        g = np.fliplr(g)

class Grid:
    def __init__(self):
        self.grid = {}
        # initialize grid
        s = iter('.#...####')
        for y in range(3):
            for x in range(3):
                #self.grid[y,x] = {'.':False,'#':True}[next(s)]
                self.grid[y,x] = next(s)
        self.size = 3

    def iterate(self, rules):
        next_iter = {}
        if not self.size%2:
            for i, y in enumerate(range(0, self.size, 2)):
                for j, x in enumerate(range(0, self.size, 2)):
                    s = ''.join([self.grid[yi, xi] 
                        for yi in range(y,y+2)
                        for xi in range(x,x+2)])
                    m = pattern_equivalent(s, rules)
                    enh = iter(rules[m])
                    for yi in range(3*i,3*i+3):
                        for xi in range(3*j,3*j+3):
                            next_iter[yi,xi] = next(enh)
            self.size = (self.size//2)*3
        else:
            for i, y in enumerate(range(0, self.size, 3)):
                for j, x in enumerate(range(0, self.size, 3)):
                    s = ''.join([self.grid[yi, xi] 
                        for yi in range(y,y+3)
                        for xi in range(x,x+3)])
                    m = pattern_equivalent(s, rules)
                    enh = iter(rules[m])
                    for yi in range(4*i,4*i+4):
                        for xi in range(4*j,4*j+4):
                            next_iter[yi,xi] = next(enh)
            self.size = (self.size//3)*4
        self.grid = next_iter

    def print(self):
        for y in range(self.size):
            for x in range(self.size):
                sys.stdout.write(self.grid[y,x])
            sys.stdout.write('\n')
        sys.stdout.write('\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    rules = {}
    with open(args.FILE, 'r') as f:
        for line in f:
            m, e = line.strip('\n').split(' => ')
            rules[m.replace('/', '')] = e.replace('/', '')
    grid = Grid()
    for i in range(18):
        grid.iterate(rules)
        if i == 4:
            print(sum(v == '#' for v in grid.grid.values()))
    print(sum(v == '#' for v in grid.grid.values()))

