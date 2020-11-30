#!/usr/bin/env python3

from .input import get_input

def manhattan_distance(p):
    return sum(abs(i) for i in p)

def signal_distance(w1, w2):
    def dist(p):
        return w1.path.index(p) + w2.path.index(p)
    return dist

class Wire:
    def __init__(self, path):
        self.path = [(0,0)]
        for m in path.split(','):
            d = m[0]
            l = int(m[1:])
            for _ in range(l):
                step = {
                        'L':(-1,0),
                        'R':(1,0),
                        'U':(0,1),
                        'D':(0,-1),
                        }[d]
                last = self.path[-1]
                self.path.append((last[0] + step[0], last[1] + step[1]))

    def intersection(self, wire2, key):
        z = set(self.path).intersection(set(wire2.path))
        return key(min(z - set([(0,0)]), key = key))

def test(args):
    def min_dist(p1, p2, value):
        w1 = Wire(p1)
        w2 = Wire(p2)
        assert w1.intersection(w2, manhattan_distance) == value
    min_dist('R8,U5,L5,D3', 'U7,R6,D4,L4', 6)
    min_dist('R75,D30,R83,U83,L12,D49,R71,U7,L72',
            'U62,R66,U55,R34,D71,R55,D58,R83', 159)
    min_dist('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
            'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 135)
    def min_sig_dist(p1, p2, value):
        w1 = Wire(p1)
        w2 = Wire(p2)
        sd = signal_distance(w1, w2)
        assert w1.intersection(w2, sd) == value
    min_sig_dist('R75,D30,R83,U83,L12,D49,R71,U7,L72',
            'U62,R66,U55,R34,D71,R55,D58,R83', 610)
    min_sig_dist('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
            'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 410)
    print('Tests passed')

def main(args):
    w1, w2 = [Wire(l) for l in get_input(args.YEAR, args.DAY)]
    print(w1.intersection(w2, manhattan_distance))
    sd = signal_distance(w1, w2)
    print(w1.intersection(w2, sd))

