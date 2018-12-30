#!/usr/bin/env python3

import argparse
import functools
import operator

class Knot:
    def __init__(self):
        self.length = 256
        self.values = list(range(self.length))
        self.skip = self.position = 0

    def twist(self, length):
        r = range(self.position, self.position + length)
        for i, j in list(zip(r, reversed(r)))[:length//2]:
            i, j = i%self.length, j%self.length
            self.values[i], self.values[j] = self.values[j], self.values[i]
        self.position = (self.position + length + self.skip) % self.length
        self.skip += 1

    def ascii_twist(self, s):
        lengths = [ord(c) for c in s] + [17,31,73,47,23]
        for _ in range(64):
            for length in lengths:
                self.twist(length)

    def binary_hash(self):
        blocks = []
        for i in range(0,256,16):
            blocks.append(functools.reduce(operator.xor, self.values[i:i+16]))
        return ''.join('{:08b}'.format(b) for b in blocks)

def get_regions(disk):
    filled = set([i for i, v in disk.items() if v == '1'])
    regions = []

    def get_neighbours(i, j):
        for p in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if p in disk:
                yield p, disk[p]

    while filled:
        visited = set()
        to_visit = set()
        p = filled.pop()
        visited.add(p)
        to_visit.update(set([i for i, v in get_neighbours(*p) if v == '1' and i not in visited]))
        while to_visit:
            p = to_visit.pop()
            visited.add(p)
            to_visit.update(set([i for i, v in get_neighbours(*p) if v == '1' and i not in visited]))
        regions.append(visited)
        filled -= visited
    return regions
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUT', nargs = '?', default = 'vbqugkhl')
    args = parser.parse_args()
    disk = {}
    for i in range(128):
        k = Knot()
        s = '{}-{}'.format(args.INPUT, i)
        k.ascii_twist(s)
        b_hash = k.binary_hash()
        for j, v in enumerate(b_hash):
            disk[i,j] = v
    print(sum(1 for i in disk.values() if i == '1'))
    print(len(get_regions(disk)))
