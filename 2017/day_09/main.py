#!/usr/bin/env python3

import argparse

class Group:
    def __init__(self, stream):
        self.groups = []
        self.garbage = []
        escaped = False
        garbage = False
        for i in stream:
            if escaped:
                escaped = False
                continue
            if i == '!':
                escaped = True
                continue
            if garbage:
                if i == '>':
                    garbage = False
                    continue
                self.garbage.append(i)
                continue
            if i == '<':
                garbage = True
                continue
            if i == '}':
                return
            if i == '{':
                self.groups.append(Group(stream))

    def score(self, n = 1):
        return n + sum(g.score(n + 1) for g in self.groups)

    def garbage_chars(self):
        return len(self.garbage) + sum(g.garbage_chars() for g in self.groups)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        stream = iter(f.read().rstrip('\n'))
    groups = []
    for i in stream:
        if i == '{':
            groups.append(Group(stream))
            continue
        print('Error')
    print(sum(g.score() for g in groups))
    print(sum(g.garbage_chars() for g in groups))
