#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        steps = f.read().strip().split(',')
    m = n = e = 0
    for s in steps:
        if 'n' in s:
            n += 1
        elif 's' in s:
            n -= 1
        if 'e' in s:
            e += 1
        elif 'w' in s:
            e -= 1
        m = max(m, abs(n), abs(e))
    print(max(abs(n), abs(e)))
    print(m)

