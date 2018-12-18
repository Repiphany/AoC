#!/usr/bin/env python3

import collections
import sys

def neighbours(y, x):
    return [
            (y-1, x-1),
            (y-1, x),
            (y-1, x+1),
            (y, x+1),
            (y+1, x+1),
            (y+1, x),
            (y+1, x-1),
            (y, x-1),
            ]

def change(lumber):
    next_lumber = {}
    for pos, v in lumber.items():
        adjacent = collections.Counter([lumber[(i, j)] for i, j in
            neighbours(*pos) if (i, j) in lumber])
        if v == '.':
            if adjacent['|'] >= 3:
                next_lumber[pos] = '|'
            else:
                next_lumber[pos] = '.'
        if v == '|':
            if adjacent['#'] >= 3:
                next_lumber[pos] = '#'
            else:
                next_lumber[pos] = '|'
        if v == '#':
            if adjacent['#'] >= 1 and adjacent['|'] >= 1:
                next_lumber[pos] = '#'
            else:
                next_lumber[pos] = '.'
    lumber.update(next_lumber)

if __name__ == '__main__':
    lumber = {}
    with open('input', 'r') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.rstrip('\n')):
                lumber[(y, x)] = c
    y_max = y + 1
    x_max = x + 1
    def lumber_str(lumber):
        def ordered():
            for y in range(y_max):
                for x in range(x_max):
                    yield lumber[(y, x)]
        return ''.join(i for i in ordered())
    seen = [lumber_str(lumber)]
    for i in range(10):
        change(lumber)
        seen.append(lumber_str(lumber))
    c = collections.Counter(lumber.values())
    print(c['|']*c['#'])

    # part 2
    while True:
        change(lumber)
        ls = lumber_str(lumber)
        if ls in seen:
            break
        seen.append(ls)
    # cycle length
    c = len(seen) - seen.index(ls)
    N = 1000000000
    ls_final = collections.Counter(seen[(N - seen.index(ls))%c + seen.index(ls)])
    print(ls_final['#']*ls_final['|'])

