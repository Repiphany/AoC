#!/usr/bin/env python3

from fractions import Fraction as F
import math
from .input import get_input
from IPython.terminal.embed import InteractiveShellEmbed
import matplotlib.pyplot as plt

class Field:
    def __init__(self, mapdata):
        self.asteroids = set()
        for i, line in enumerate(mapdata):
            for j, v in enumerate(line):
                if v == '#':
                    self.asteroids.add((j, i))

    def line_of_sight(self, a, b):
        # print integer coordinates on line of site from a to b
        ax, ay = a
        bx, by = b
        dy = by - ay
        dx = bx - ax
        k = math.gcd(dy, dx)
        dy //= k
        dx //= k
        for i in range(1,k):
            yield (ax + i*dx, ay + i*dy)

    def visible_from(self, a, b):
        return not any(pt in self.asteroids for pt in self.line_of_sight(a, b))

    def visible(self, a):
        N = 0
        for b in self.asteroids - set([a]):
            if not self.visible_from(a, b):
                continue
            N += 1
        return N

    def vaporize_order(self, a):
        order = []
        def sorter(b):
            dx = b[0] - a[0]
            dy = b[1] - a[1]
            return (-math.atan2(dx, dy), dx**2 + dy**2)
        while len(self.asteroids) > 1:
            for b in sorted(self.asteroids - set([a]) - set(order), key = sorter):
                if self.visible_from(a, b):
                    order.append(b)
            self.asteroids -= set(order)
        return order
        
def test(args):
    field = Field('.#..#\n.....\n#####\n....#\n...##'.split('\n'))
    assert max(field.asteroids, key = field.visible) == (3,4)
    field = Field("""......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
""".split('\n'))
    assert max(field.asteroids, key = field.visible) == (5,8)
    field = Field(""".#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".split('\n'))
    assert field.vaporize_order((11,13))[199] == (8,2)
    print('Tests passed')


def main(args):
    field = Field(get_input(args.YEAR, args.DAY))
    pt = max(field.asteroids, key = field.visible)
    print(field.visible(pt))
    bet = field.vaporize_order(pt)[199]
    print(bet[0]*100+bet[1])

