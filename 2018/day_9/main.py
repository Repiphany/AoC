#!/usr/bin/env python3

import re
import collections

def highest_scorer(N, M):
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

    # part 1
    highest_scorer(N, M)

    # part 2
    highest_scorer(N, M*100)
