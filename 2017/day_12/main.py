#!/usr/bin/env python3

import argparse
import collections

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()

    connections = collections.defaultdict(set)
    with open(args.FILE, 'r') as f:
        for line in f:
            line = line.strip()
            a = int(line.split(' ')[0])
            b = [int(i) for i in line.split('<-> ')[-1].split(', ')]
            connections[a].update(b)
            for bi in b:
                connections[bi].add(a)

    def get_group(n):
        seen = set([n])
        looking = set(connections[n])
        while looking:
            t = looking.pop()
            seen.add(t)
            looking.update(connections[t] - seen)
        return seen
    print(len(get_group(0)))

    ungrouped = set(connections.keys())
    groups = []
    while ungrouped:
        p = ungrouped.pop()
        g = get_group(p)
        ungrouped -= g
        groups.append(g)
    print(len(groups))
