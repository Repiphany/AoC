#!/usr/bin/env python3

import argparse
import itertools

def redistribute(banks):
    v = max(banks)
    idx = banks.index(v)
    banks[idx] = 0
    for i in range(1, v + 1):
        banks[(idx + i)%len(banks)] += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        banks = [int(i) for i in f.read().split('\t')]
    seen = [tuple(banks)]
    for n in itertools.count(start = 1):
        redistribute(banks)
        if tuple(banks) in seen:
            break
        seen.append(tuple(banks))
    print(n)
    c_i = tuple(banks)
    for c in itertools.count(start = 1):
        redistribute(banks)
        if tuple(banks) == c_i:
            break
    print(c)


