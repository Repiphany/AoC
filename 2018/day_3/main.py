#!/usr/bin/env python3

import re
import collections

def part_1(claims):
    claimed = collections.defaultdict(list)
    for elf, (x, y, w, h) in claims.items():
        for xi in range(x, x + w):
            for yi in range(y, y + h):
                claimed[(xi, yi)].append(elf)
    print(sum(1 for v in claimed.values() if len(v) >= 2))

if __name__ == '__main__':
    claims = {}
    with open('input', 'r') as f:
        for line in f:
            elf, x, y, w, h = [int(i) for i in re.findall(r'\d+', line)]
            claims[elf] = (x, y, w, h)
    part_1(claims)
