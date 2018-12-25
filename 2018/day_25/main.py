#!/usr/bin/env python3

import numpy as np

def manhattan_distance(x, y):
    x = np.asarray(x)
    y = np.asarray(y)
    return np.sum(np.abs(x - y))

if __name__ == '__main__':
    pts = []
    with open('input', 'r') as f:
        for line in f:
            pts.append(tuple([int(i) for i in line.split(',')]))

    constellations = []

    def integrate_pt(pt, constellations = constellations):
        connected = []
        for constellation in constellations:
            if any(manhattan_distance(c, pt) <= 3 for c in constellation):
                connected.append(constellation)
        if len(connected) == 0:
            constellations.append(set([pt]))
        elif len(connected) == 1:
            connected[0].add(pt)
        elif len(connected) > 1:
            for c in connected:
                constellations.remove(c)
            constellations.append(set.union(set([pt]), *connected))

    for pt in pts:
        integrate_pt(pt)
    print(len(constellations))
