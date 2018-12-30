#!/usr/bin/env python3

import argparse
import collections

def spinlock(step, N):
    ring = collections.deque([])
    zero = set()
    for i in range(N + 1):
        if not i%100000:
            print(i)
        ring.rotate(-step)
        ring.append(i)
        #az = ring[(ring.index(0) + 1)%len(ring)]
        #if az not in zero:
        #    print(i, az)
        #    zero.add(az)
    return ring

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('INPUT', nargs = '?', default = 367, type = int)
    args = parser.parse_args()
    ring = spinlock(args.INPUT, 2017)
    print(ring[0])
    ring = spinlock(args.INPUT, 50000000)
    print(ring[ring.index(0) + 1])

