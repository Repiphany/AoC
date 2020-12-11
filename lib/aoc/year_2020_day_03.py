#!/usr/bin/env python3

from .input import get_input
from IPython.terminal.embed import InteractiveShellEmbed
import collections

class Geology:
    def __init__(self, s):
        self.trees = collections.defaultdict(bool)
        for y, line in enumerate(s):
            for x, v in enumerate(line):
                self.trees[x,y] = (v == '#')
        self.height = y + 1
        self.width = x + 1

    def __getitem__(self, k):
        x, y = k
        return self.trees[(x%self.width, y)]

    def traverse(self, dx, dy):
        for i in range(self.height//dy + 1):
            yield self[(dx*i, dy*i)]

def test(args):
    s = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    geology = Geology(s.split('\n'))
    assert sum(geology.traverse(3, 1)) == 7
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    prod = 1
    for m in slopes:
        prod *= sum(geology.traverse(*m))
    assert prod == 336
    print('Tests passed')

def main(args):
    shell = InteractiveShellEmbed()
    geology = Geology(get_input(args.YEAR, args.DAY))
    print(sum(geology.traverse(3,1)))
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    prod = 1
    for m in slopes:
        prod *= sum(geology.traverse(*m))
    print(prod)

