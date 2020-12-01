#!/usr/bin/env python3

from .input import get_input
from .intcode import Intcode
from collections import defaultdict
import itertools
from IPython.terminal.embed import InteractiveShellEmbed
import matplotlib.pyplot as plt
import numpy as np

class Popper:
    def __init__(self, value):
        self.value = value

    def pop(self, *args, **kwargs):
        return self.value

class Robot:
    def __init__(self, prog):
        self.ic = Intcode(prog)
        self.ic.return_output = True
        self.panels = defaultdict(int)
        self.pos = 0 + 0j
        self.facing = 0 + 1j

    def turn_left(self):
        #print('Turn left')
        self.facing *= 1j

    def turn_right(self):
        #print('Turn right')
        self.facing *= -1j

    def move_forward(self):
        self.pos += self.facing

    def run(self):
        self.painted = set()
        while True:
            try:
                value = Popper(self.panels[self.pos])
                self.ic.value = value
                self.panels[self.pos] = self.ic.run()
                value = Popper(self.panels[self.pos])
                self.ic.value = value
                self.painted.add(self.pos)
                # turn
                {0:self.turn_left, 1:self.turn_right}[self.ic.run()]()
                self.move_forward()
            except KeyError:
                pass
            if self.ic.halted:
                break
        return self.painted

def test(args):
    print('Tests passed')

def main(args):
    robot = Robot(next(get_input(args.YEAR, args.DAY)))
    print(len(robot.run()))

    robot2 = Robot(next(get_input(args.YEAR, args.DAY)))
    robot2.panels[0j] = 1
    robot2.run()
    w = np.array([i for i, v in robot2.panels.items() if v])
    fig, ax = plt.subplots(1, 1)
    ax.set_aspect('equal')
    ax.plot(w.real, w.imag, marker = 's', linestyle = '')
    plt.show()

