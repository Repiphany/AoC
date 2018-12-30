#!/usr/bin/env python3

import argparse
import re
import itertools

class Particle:
    N = 0
    def __init__(self, s):
        (
                self.x, self.y, self.z,
                self.vx, self.vy, self.vz,
                self.ax, self.ay, self.az
                ) = [int(i) for i in re.findall(r'-?\d+', s)]
        self.n = Particle.N
        Particle.N += 1
        self.collided = False

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.z == other.z

    def tick(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def dist(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        particles = [Particle(line) for line in f]
    for _ in range(500): # should find a heuristic for "long term"
        for p in particles:
            p.tick()
    print(min(particles, key = lambda x : x.dist()).n)

    Particle.N = 0
    with open(args.FILE, 'r') as f:
        particles = [Particle(line) for line in f]
    for tick in range(50): # No concrete determination of when particles stop colliding
        for p in particles:
            p.tick()
        for p1, p2 in itertools.combinations(particles, 2):
            if p1 == p2:
                p1.collided = p2.collided = True
        for p in particles[:]:
            if p.collided:
                particles.remove(p)
    print(len(particles))


