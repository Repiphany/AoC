#!/usr/bin/env python3

import re
import collections

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
    y_max = max(y for (y, x) in clay)
    y_min = min(y for (y, x) in clay)
    source = (0, 500)
    filled = set()
    flow_down = [source]
    fill_horizontal = []

    def is_filled(pos):
        return (pos in clay) or (pos in filled)

    def flowfill():
        while flow_down:
            y, x = pos = flow_down.pop()
            fill_horizontal.append(pos)
            while True:
                y += 1
                if (y, x) in clay:
                    break
                filled.add((y, x))
                if y == y_max:
                    return True
                fill_horizontal.append((y, x))
        if not fill_horizontal:
            return False
        y, x = pos = fill_horizontal.pop()
        left_overflow = right_overflow = False
        do_fill = True
        xl = x
        while True:
            xl -= 1
            if (y, xl) in clay:
                xl += 1
                break
            if not is_filled((y+1, xl)):
                if (y + 1, xl + 1) in clay:
                    left_overflow = True
                else:
                    do_fill = False
                break
        xr = x
        while True:
            xr += 1
            if (y, xr) in clay:
                xr -= 1
                break
            if not is_filled((y + 1, xr)):
                if (y + 1, xr - 1) in clay:
                    right_overflow = True
                else:
                    do_fill = False
                break
        if do_fill:
            for xi in range(xl, xr + 1):
                filled.add((y, xi))
            if left_overflow:
                flow_down.append((y, xl))
            if right_overflow:
                flow_down.append((y, xr))
        return True

    # part 1
    while flowfill():
        pass
    print(len([y for (y, x) in filled if y_min <= y <= y_max]))

    # part 2
    while True:
        changed = False
        for (y, x) in filled.copy():
            if not all(is_filled(n) for n in [(y+1,x),(y,x+1),(y,x-1)]):
                try:
                    filled.remove((y, x))
                    xl = x - 1
                    xr = x + 1
                    while (y, xl) in filled:
                        filled.remove((y, xl))
                        xl -= 1
                    while (y, xr) in filled:
                        filled.remove((y, xr))
                        xl += 1
                    changed = True
                except:
                    continue
        if not changed:
            break
    print(len([y for (y, x) in filled if y_min <= y <= y_max]))
