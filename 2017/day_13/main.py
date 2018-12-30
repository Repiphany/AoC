#!/usr/bin/env python3

import argparse
import itertools

def severity(layers):
    s = 0
    for k, v in layers.items():
        if not k % ((v-1)*2):
            s += k*v
    return s

def caught(layers, delay):
    for k, v in layers.items():
        if not (k + delay) % ((v-1)*2):
            return True
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    layers = {}
    with open(args.FILE, 'r') as f:
        for line in f:
            a, b = [int(i) for i in line.strip().split(': ')]
            layers[a] = b
    print(severity(layers))
    for delay in itertools.count():
        if not caught(layers, delay):
            break
    print(delay)

