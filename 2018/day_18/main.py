#!/usr/bin/env python3

import collections

def neighbours(y, x):
    return [(y-1, x-1), (y-1, x), (y-1, x+1), (y, x+1),
            (y+1, x+1), (y+1, x), (y+1, x-1), (y, x-1)]

def change(lumber):
    next_lumber = {}
    for pos, v in lumber.items():
        adjacent = collections.Counter([lumber[(i, j)] for i, j in
            neighbours(*pos) if (i, j) in lumber])
        if v == '.':
            next_lumber[pos] = '|' if adjacent['|'] >= 3 else '.'
        if v == '|':
            next_lumber[pos] = '#' if adjacent['#'] >= 3 else '|'
        if v == '#':
            next_lumber[pos] = '#' if adjacent['#']*adjacent['|'] else '.'
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
        return ''.join(lumber[(y, x)]
                for y in range(y_max) for x in range(x_max))
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
    c_start = seen.index(ls)
    c_length = len(seen) - seen.index(ls)
    N = 1000000000
    ls_N = collections.Counter(seen[(N - c_start)%c_length + c_start])
    print(ls_N['#']*ls_N['|'])

