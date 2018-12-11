#!/usr/bin/env python3

import numpy as np
import time

def total_power(x, y, puzzle_input):
    rack_id = x + 10
    power_level = rack_id*y
    power_level += puzzle_input
    power_level *= rack_id
    power_level = int(str(power_level)[-3]) if power_level >= 100 else 0
    power_level -= 5
    return power_level

def grid_integral(g):
    """Returns an array g_I such that g_i([y+1, x+1]) = np.sum(g[:y, :x])"""
    g_I = np.zeros(tuple(x + 1 for x in g.shape), dtype = g.dtype)
    for (y, x), v in np.ndenumerate(np.cumsum(g, axis = 1)):
        g_I[(y+1, x+1)] = v + g_I[(y, x+1)]
    return g_I

def main(puzzle_input, N = 300):
    grid = np.zeros((N, N), dtype = int)
    for i, _ in np.ndenumerate(grid):
        grid[i] = total_power(i[0] + 1, i[1] + 1, puzzle_input)
    g_I = grid_integral(grid)
    def total(upper_left, size, g_I = g_I):
        # returns the sum of elements in the window
        # upper_left -> upper left + size
        y, x = upper_left
        return (g_I[(y, x)] + g_I[(y + size, x + size)]
                - g_I[(y, x + size)] - g_I[(y + size, x)])

    # only check window size up to specified max
    windowed_sums = {}
    window_max = 20
    for size in range(1, window_max + 1):
        width = N - size + 1
        g_s = np.zeros((width, width), dtype = int)
        windowed_sums[size] = g_s
        for i, _ in np.ndenumerate(g_s):
            g_s[i] = total(i, size)

    def ndim_argmax(g, offset = 0):
        return tuple(offset+i for i in np.unravel_index(np.argmax(g), g.shape))

    # part 1
    y, x = ndim_argmax(windowed_sums[3], offset = 1)
    print('{},{}'.format(y, x))

    # part 2
    s, g = sorted(windowed_sums.items(), key = lambda x : np.max(x[1]))[-1]
    y, x = ndim_argmax(g, offset = 1)
    print('{},{},{}'.format(y,x,s))

if __name__ == '__main__':
    puzzle_input = 9221
    main(puzzle_input)
