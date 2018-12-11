#!/usr/bin/env python3

import collections
import numpy as np

def total_power(x, y, puzzle_input):
    rack_id = x + 10
    power_level = rack_id*y
    power_level += puzzle_input
    power_level *= rack_id
    power_level = int(str(power_level)[-3]) if power_level >= 100 else 0
    power_level -= 5
    return power_level

def part_1(puzzle_input):
    grid = np.zeros((300, 300))
    for i, _ in np.ndenumerate(grid):
        grid[i] = total_power(i[0] + 1, i[1] + 1, puzzle_input)
    cells = np.zeros((298, 298))
    for i, _ in np.ndenumerate(cells):
        cells[i] = np.sum(grid[i[0]:i[0]+3,i[1]:i[1]+3])
    print(np.array(np.unravel_index(np.argmax(cells), cells.shape)) + 1)
    print(np.max(cells))

if __name__ == '__main__':
    puzzle_input = 9221
    part_1(puzzle_input)
