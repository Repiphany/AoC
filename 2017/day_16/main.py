#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        moves = f.read().strip().split(',')
    programs = list('abcdefghijklmnop')

    def spin(programs, x):
        return programs[-x:] + programs[:-x]

    def exchange(programs, a, b):
        programs[a], programs[b] = programs[b], programs[a]
        return programs

    def partner(programs, a, b):
        i, j = programs.index(a), programs.index(b)
        return exchange(programs, i, j)

    def perform_dance(programs, moves):
        for move in moves:
            if move.startswith('s'):
                programs = spin(programs, int(move[1:]))
            elif move.startswith('x'):
                a, b = [int(i) for i in move[1:].split('/')]
                programs = exchange(programs, a, b)
            else:
                a, b = move[1:].split('/')
                programs = partner(programs, a, b)
        return programs
    programs = perform_dance(programs, moves)
    print(''.join(programs))

    programs = list('abcdefghijklmnop')
    seen = []
    while True:
        seen.append(''.join(programs))
        programs = perform_dance(programs, moves)
        if ''.join(programs) in seen:
            print(seen.index(''.join(programs)))
            break
    c = len(seen) - seen.index(''.join(programs))
    print(len(seen))

    programs = list('abcdefghijklmnop')
    for i in range(1000000000%c):
        programs = perform_dance(programs, moves)
    print(''.join(programs))
