#!/usr/bin/env python3

from .input import get_input

class Structure:
    def __init__(self, lines):
        self.actions = [(line[0], int(line[1:])) for line in lines if line.strip()]
        self.facing = 1
        self.position = 0 + 0j
        self.waypoint_position = 10 + 1j

    def initialize(self):
        self.facing = 1
        self.position = 0 + 0j
        self.waypoint_position = 10 + 1j

    def do_action(self, action, waypoint = False):
        c, v = action
        dirs = {'N':1j, 'S':-1j, 'E':1, 'W': -1}
        rots = {'L':1j, 'R':-1j}
        if c in 'NSWE':
            m = dirs[c]
            if waypoint:
                self.waypoint_position += m*v
            else:
                self.position += m*v
        elif c in 'LR':
            r = rots[c]**(v//90)
            if waypoint:
                self.waypoint_position *= r
            else:
                self.facing *= r
        elif c == 'F':
            if waypoint:
                self.position += self.waypoint_position*v
            else:
                self.position += self.facing*v

    def run(self, waypoint = False):
        self.initialize()
        for action in self.actions:
            self.do_action(action, waypoint = waypoint)
        return self.manhattan_distance

    @property
    def manhattan_distance(self):
        return int(abs(self.position.real) + abs(self.position.imag))

def test(args):
    structure = Structure("F10 N3 F7 R90 F11".split(' '))
    assert structure.run() == 25
    assert structure.run(waypoint = True) == 286
    print('Tests passed')

def main(args):
    structure = Structure(get_input(args.YEAR, args.DAY))
    print(structure.run())
    print(structure.run(waypoint = True))

