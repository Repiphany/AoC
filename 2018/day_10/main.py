#!/usr/bin/env python3

import re
import numpy as np
import scipy.optimize
import sys

def moment(positions):
    center_of_mass = np.average(positions, axis = 0)
    return np.sum((positions - center_of_mass)**2)

def part_1(positions, velocities):
    f = lambda i : moment(positions + i*velocities)
    res = scipy.optimize.minimize(f, x0 = 0)
    pos_final = positions + int(res.x)*velocities
    x_min, y_min = np.min(pos_final, axis = 0).astype(int)
    x_max, y_max = np.max(pos_final, axis = 0).astype(int)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if np.any(np.all((x, y) == pos_final, axis = 1)):
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

if __name__ == '__main__':
    positions, velocities = [], []
    with open('input', 'r') as f:
        for line in f:
            x, y, vx, vy = [int(i) for i in re.findall(r'-?\d+', line)]
            positions.append((x, y))
            velocities.append((vx, vy))
    positions = np.asarray(positions, dtype = float)
    velocities = np.asarray(velocities, dtype = float)

    part_1(positions, velocities)

