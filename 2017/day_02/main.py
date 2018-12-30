#!/usr/bin/env python3

import argparse
import itertools

def checksum(rows):
    s = 0
    for row in rows:
        r = [int(i) for i in row.split('\t')]
        s += (max(r) - min(r))
    return s

def div_checksum(rows):
    s = 0
    for row in rows:
        for a, b in itertools.combinations((int(i) for i in row.split('\t')), 2):
            a, b = sorted((a, b))
            if not b%a:
                s += b//a
                break
    return s


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        rows = f.readlines()
    print(checksum(rows))
    print(div_checksum(rows))
