#!/usr/bin/env python3

import argparse
import operator
import functools

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

    def dense_hash(self):
        blocks = []
        for i in range(0,256,16):
            blocks.append(functools.reduce(operator.xor, self.values[i:i+16]))
        return ''.join('{:02x}'.format(b) for b in blocks)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        s = f.read().strip()
        lengths = [int(i) for i in s.split(',')]
    k = Knot()
    for length in lengths:
        k.twist(length)
    print(k.values[0]*k.values[1])

    k2 = Knot()
    lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
    for _ in range(64):
        for length in lengths:
            k2.twist(length)
    print(k2.dense_hash())
