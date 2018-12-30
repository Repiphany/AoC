#!/usr/bin/env python3

import argparse

def escape(offsets):
    i = 0
    jumps = 0
    while True:
        try:
            o = offsets[i]
            offsets[i] += 1
            i += o
            jumps += 1
        except IndexError:
            return jumps

def escape_2(offsets):
    i = 0
    jumps = 0
    while True:
        try:
            o = offsets[i]
            offsets[i] += 1 if o < 3 else -1
            i += o
            jumps += 1
        except IndexError:
            return jumps

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        offsets = [int(i) for i in f]
    print(escape(offsets[:]))
    print(escape_2(offsets[:]))
