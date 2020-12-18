#!/usr/bin/env python3

from .input import get_input_line

class Game:
    def __init__(self, line):
        self.numbers = [int(i) for i in line.split(',')]

    def play(self, N):
        spoken = {n: i for i, n in enumerate(self.numbers[:-1], start = 1)}
        n = self.numbers[-1]
        for i in range(len(self.numbers), N):
            spoken[n], n = i, 0 if n not in spoken else i - spoken[n]
        return n

def test(args):
    N = 30000000
    assert Game("0,3,6").play(N) == 175594
    assert Game('1,2,3').play(N) == 261214
    print('Tests passed')

def main(args):
    game = Game(get_input_line(args.YEAR, args.DAY))
    print(game.play(2020))
    print(game.play(30000000))

