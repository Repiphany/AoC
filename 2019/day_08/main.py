#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

class SIF:
    def __init__(self, fname, width = 25, height = 6):
        with open('input', 'r') as f:
            self.data = [int(i) for i in f.read().strip()]
        self.width = width
        self.height = height
        self.data = np.asarray(self.data)
        self.layers = self.data.reshape(-1, height, width)

    def collapse(self):
        self.collapsed = np.zeros((self.height, self.width)).astype(int) - 1
        for idx, v in np.ndenumerate(self.layers):
            l, h, w = idx
            if self.collapsed[(h, w)] == -1:
                # not filled yet
                if v != 2:
                    self.collapsed[(h, w)] = v
        return self.collapsed

if __name__ == '__main__':
    sif = SIF('input')
    # part 1
    zero_min_layer = np.argmin((sif.layers.reshape(-1, sif.width*sif.height) == 0).sum(axis = 1))
    l = sif.layers[zero_min_layer]
    print(np.sum(l == 1)*np.sum(l == 2))
    # part 2
    plt.imshow(sif.collapse())
    plt.show()

