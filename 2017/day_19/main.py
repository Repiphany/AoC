#!/usr/bin/env python3

import argparse
import collections
import itertools

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    track = {}
    start = None
    with open(args.FILE, 'r') as f:
        for y, line in enumerate(f):
            line = line.rstrip('\n')
            for x, c in enumerate(line):
                if c != ' ':
                    if start is None:
                        start = (y, x)
                    track[y, x] = c
    v = [1, 0] # [dy, dx]
    seen = []
    y, x = start
    for step in itertools.count(start = 1):
        dy, dx = v
        y += dy
        x += dx
        try:
            c = track[y, x]
        except KeyError:
            break
        if c in '|-':
            continue
        if c == '+':
            if dy:
                v = [0, 1 if track.get((y, x + 1)) else -1]
            elif dx:
                v = [1 if track.get((y + 1, x)) else -1, 0]
        else:
            seen.append(c)
    print(''.join(seen))
    print(step)

