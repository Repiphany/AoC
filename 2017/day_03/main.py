#!/usr/bin/env python3

import argparse
import math
import collections

def cmod(n, m):
    q, r = divmod(n, m)
    return r if q%2 else m - r

def grid_dist(n):
    r = math.ceil(n**0.5)//2
    i = (2*r + 1)**2
    return r + cmod(n - i, r)

def grid_allocate():
    grid = collections.defaultdict(int)
    def neighbours(x, y):
        return [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),
                (x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1)]
    grid[0,0]=1
    def spiral():
        x = y = 0
        r = 1
        while True:
            while x < r:
                x += 1
                yield (x, y)
            while y < r:
                y += 1
                yield (x, y)
            while x > -r:
                x -= 1
                yield (x, y)
            while y > -r:
                y -= 1
                yield (x, y)
            r += 1
    for x, y in spiral():
        grid[x, y] = sum(grid[xi,yi] for xi,yi in neighbours(x, y))
        yield grid[x, y]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUT', nargs = '?', default = 312051, type = int)
    args = parser.parse_args()
    print(grid_dist(args.INPUT))
    for v in grid_allocate():
        if v > args.INPUT:
            print(v)
            break
