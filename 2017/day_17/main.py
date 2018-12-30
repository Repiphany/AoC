#!/usr/bin/env python3

import argparse
import collections

def spinlock(step, N):
    ring = collections.deque([])
    zero = set()
    for i in range(N + 1):
        ring.rotate(-step)
        ring.append(i)
    return ring

def spinlock_zero(step, N):
    zero_index = 0
    zero_n = 0
    pos = 0
    for i in range(1, N + 1):
        pos = (pos + step)%(i) + 1
        if pos == zero_index + 1:
            zero_n = i
        if pos <= zero_index:
            zero_index += 1
    return zero_n


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUT', nargs = '?', default = 367, type = int)
    args = parser.parse_args()
    ring = spinlock(args.INPUT, 2017)
    print(ring[0])
    zn = spinlock_zero(args.INPUT, 50000000)
    print(zn)

