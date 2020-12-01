#!/usr/bin/env python3

from .input import get_input
import numpy as np
import matplotlib.pyplot as plt

def test(args):
    print('Tests passed')

def main(args):
    image = np.array([int(i) for i in next(get_input(args.YEAR,
        args.DAY)).strip()])
    width = 25
    height = 6
    image = image.reshape((-1, width*height))
    l = np.argmin(np.sum(image == 0, axis = 1))
    print((np.sum(image == 1, axis = 1)*np.sum(image == 2, axis = 1))[l])
    image = image.reshape((-1, height, width))
    decoded = image[0]
    for layer in image[1:]:
        idx = (decoded == 2)
        decoded[idx] = layer[idx]
    plt.imshow(decoded, aspect = 'equal')

