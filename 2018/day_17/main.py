#!/usr/bin/env python3

import re
import collections

class Reservoir:
    def __init__(self, clay):
        self.clay = clay
        self.y_max = max(y for (y, x) in clay)
        self.y_min = min(y for (y, x) in clay)
        source = (0, 500)
        self.filled = set()
        self.flow_down = [source]
        self.line = None
        self.to_fill = []

    def is_filled(self, position):
        return position in self.clay or position in self.filled

    def flowfill(self):
        while self.flow_down:
            y, x = self.flow_down.pop()
            self.to_fill.append((y, x))
            while True:
                y += 1
                if (y, x) in self.clay:
                    break
                self.filled.add((y, x))
                if y == self.y_max:
                    return True
                self.to_fill.append((y, x))
        if not self.to_fill:
            return False
        y, x = self.to_fill.pop()
        left_overflow = False
        right_overflow = False
        fill = True
        xl = x
        while True:
            xl -= 1
            if (y, xl) in self.clay:
                xl += 1
                break
            if not self.is_filled((y + 1, xl)):
                if (y + 1, xl + 1) in self.clay:
                    left_overflow = True
                    break
                else:
                    fill = False
                    break
        xr = x
        while True:
            xr += 1
            if (y, xr) in self.clay:
                xr -= 1
                break
            if not self.is_filled((y + 1, xr)):
                if (y + 1, xr - 1) in self.clay:
                    right_overflow = True
                    break
                else:
                    fill = False
                    break
        if fill:
            for xi in range(xl, xr + 1):
                self.filled.add((y, xi))
            if left_overflow:
                self.flow_down.append((y, xl))
            if right_overflow:
                self.flow_down.append((y, xr))
        return True

    def drain(self):
        while True:
            d = False
            for (y, x) in self.filled.copy():
                n = [(y+1,x),(y,x+1),(y,x-1)]
                if not all(self.is_filled(ni) for ni in n):
                    d = True
                    self.filled.remove((y, x))
            if not d:
                return

if __name__ == '__main__':
    clay = set()
    with open('input', 'r') as f:
        for line in f:
            a, b, c = [int(i) for i in re.findall(r'\d+', line)]
            if line.startswith('x'):
                x = a
                for y in range(b, c + 1):
                    clay.add((y, x))
            else:
                y = a
                for x in range(b, c + 1):
                    clay.add((y, x))
    reservoir = Reservoir(clay)

    while reservoir.flowfill():
        pass
    print(len([y for (y, x) in reservoir.filled if reservoir.y_min <= y <= reservoir.y_max]))

    reservoir.drain()
    print(len([y for (y, x) in reservoir.filled if reservoir.y_min <= y <= reservoir.y_max]))

