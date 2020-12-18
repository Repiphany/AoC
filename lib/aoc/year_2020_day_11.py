#!/usr/bin/env python3

from .input import get_input
from collections import defaultdict

class Seats:
    def __init__(self, lines):
        self.seats = set()
        for y, line in enumerate(lines):
            line = line.strip()
            for x, c in enumerate(line):
                if c == 'L':
                    self.seats.add(x + y*1j)
        xm, ym = x + 1, y + 1

        self.adjacent = {}
        self.adjacent_view = {}
        directions = [1, 1+1j, 1j, -1+1j, -1, -1 - 1j, -1j, 1-1j]
        for x in range(xm):
            for y in range(ym):
                pos = x + y*1j
                if pos not in self.seats:
                    continue
                self.adjacent[pos] = [pos + d for d in directions
                        if pos + d in self.seats]
                def in_view(d):
                    kpos = pos + d
                    while 0 <= kpos.real < xm and 0 <= kpos.imag < ym:
                        if kpos in self.seats:
                            return kpos
                        kpos += d
                av = []
                for d in directions:
                    kpos = in_view(d)
                    if kpos:
                        av.append(kpos)
                self.adjacent_view[pos] = av

    def stabilize(self, adjacent, N):
        state = defaultdict(bool)
        while True:
            def change(s):
                occupied = state[s]
                if occupied:
                    return sum(state[a] for a in adjacent[s]) >= N
                else:
                    return not any(state[a] for a in adjacent[s])
            to_change = [s for s in self.seats if change(s)]
            if not to_change:
                return state
            for c in to_change:
                state[c] = not state[c]

def test(args):
    seats = Seats("""L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split('\n'))
    print(sum(seats.stabilize(seats.adjacent, 4).values()))
    print(sum(seats.stabilize(seats.adjacent_view, 5).values()))
    print('Tests passed')

def main(args):
    seats = Seats(get_input(args.YEAR, args.DAY))
    print(sum(seats.stabilize(seats.adjacent, 4).values()))
    print(sum(seats.stabilize(seats.adjacent_view, 5).values()))


