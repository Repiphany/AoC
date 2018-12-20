#!/usr/bin/env python3

from main import Facility
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    facility = Facility()
    with open('input', 'r') as f:
        facility.step(iter(f.read()), save_path = True)
    fig, ax = plt.subplots(1, 1, figsize = (12,10))
    x, y = zip(*facility.min_steps.keys())

    z = np.zeros((np.ptp(x) + 1, np.ptp(y) + 1), dtype = int)
    for k, v in facility.min_steps.items():
        xi, yi = k
        z[(yi + abs(min(y)), xi + abs(min(x)))] = v
    plt.imshow(z, origin = 'lower', 
            extent = (min(x) - 0.5, max(x) + 0.5, min(y) - 0.5, max(y) + 0.5))
    plt.colorbar()
    k, _ = max(facility.min_steps.items(), key = lambda x : x[1])
    longest_path = facility.min_path[k]
    xp, yp = zip(*longest_path)
    xp = np.asarray(xp)
    yp = np.asarray(yp)
    ax.plot(xp, yp, color = 'C3')
    ax.plot(xp[[0,-1]], yp[[0,-1]], marker = 'o', linestyle = '', color = 'C3')
    plt.show()
