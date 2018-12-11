#!/usr/bin/env python3

import re
import collections

def part_1(N, M):
    marble_circle = collections.deque([0])
    scores = collections.defaultdict(int)
    for i in range(1, M + 1):
        if i % 23:
            marble_circle.rotate(-2)
            marble_circle.appendleft(i)
        else:
            marble_circle.rotate(7)
            scores[i%N] += i + marble_circle.popleft()
    print(max(scores.values()))

if __name__ == '__main__':
    with open('input', 'r') as f:
        N, M = [int(i) for i in re.findall(r'\d+', f.read())]
    part_1(N, M)
