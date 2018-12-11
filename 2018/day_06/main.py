#!/usr/bin/env python3

import numpy as np

def part_1(coordinates):
    bounds = np.max(coordinates, axis = 0)
    grid = np.empty(tuple(bounds), dtype = int)
    for i, _ in np.ndenumerate(grid):
        mh_dist = np.sum(np.absolute(coordinates - i), axis = 1)
        idx = np.argsort(mh_dist)
        if mh_dist[idx[0]] < mh_dist[idx[1]]:
            grid[i] = idx[0]
        else:
            grid[i] = -1
    edges = np.s_[0,:], np.s_[-1,:], np.s_[:,0], np.s_[:,-1]
    infinite = set()
    for edge in edges:
        infinite.update(set(grid[edge]))
    print(infinite)
    areas = [np.sum(grid == i) for i in set(grid.flatten()) - infinite]
    print(sorted(areas)[-1])
    
def part_2(coordinates, safe = 10000):
    bounds = np.max(coordinates, axis = 0)
    grid = np.empty(tuple(bounds), dtype = int)
    for i, _ in np.ndenumerate(grid):
        total_mh_dist = np.sum(np.absolute(coordinates - i))
        grid[i] = total_mh_dist
    print(np.sum(grid < safe))
    
if __name__ == '__main__':
    with open('input', 'r') as f:
        coordinates = np.asarray([tuple(int(i) for i in line.split(', '))
                for line in f])
    part_1(coordinates)
    part_2(coordinates)

