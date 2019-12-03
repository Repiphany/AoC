#!/usr/bin/env python3

class Path:
    def __init__(self, path):
        self.x = [0]
        self.y = [0]
        for m in path.split(','):
            self.move(m)
        self.xy = list((i, j) for i, j in zip(self.x, self.y))

    def move(self, m):
        dx, dy = { 'U':(0, 1), 'D':(0, -1), 'L':(1, 0), 'R':(-1, 0), }[m[0]]
        for i in range(int(m[1:])):
            self.x.append(self.x[-1] + dx)
            self.y.append(self.y[-1] + dy)

def manhattan(a, b = (0, 0)):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

if __name__ == '__main__':
    with open('input', 'r') as f:
        paths = [Path(line) for line in f]
    intersections = set.intersection(*[set(p.xy) for p in paths])
    intersections.remove((0,0))

    # part 1
    print(manhattan(min(intersections, key = manhattan)))

    # part 2
    def combined_steps(i):
        return sum(p.xy.index(i) for p in paths)
    print(combined_steps(min(intersections, key = combined_steps)))

