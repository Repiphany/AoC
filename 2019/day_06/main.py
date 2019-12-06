#!/usr/bin/env python3

class Orbits:
    def __init__(self, name):
        self.name = name
        self.direct = []

    def __repr__(self):
        return '<Orbits: {}>'.format(self.name)

    def indirect(self):
        for o in self.direct:
            yield from o.direct
            yield from o.indirect()

    def map_to(self, dest, path = None):
        if path is None:
            path = []
        if dest in self.direct:
            yield path
        else:
            for o in self.direct:
                yield from o.map_to(dest, path = path + [o])

if __name__ == '__main__':
    orbits = {}
    with open('input', 'r') as f:
        for line in f:
            a, b = line.strip().split(')')
            if a not in orbits:
                orbits[a] = Orbits(a)
            if b not in orbits:
                orbits[b] = Orbits(b)
            orbits[a].direct.append(orbits[b])

    # part 1
    direct = sum(len(v.direct) for k, v in orbits.items())
    indirect = sum(len(list(v.indirect())) for k, v in orbits.items())
    print(direct + indirect)

    # part 2
    com = orbits['COM']
    san = orbits['SAN']
    you = orbits['YOU']
    to_san = next(com.map_to(san))
    to_you = next(com.map_to(you))
    common = set.intersection(set(to_san), set(to_you))
    root = max(common, key = to_san.index)
    print(len(next(root.map_to(san))) + len(next(root.map_to(you))))

