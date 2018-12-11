#!/usr/bin/env python3

import collections

def part_1(polymer):
    reacted = []
    for a in polymer:
        try:
            if abs(ord(a) - ord(reacted[-1])) == 32:
                b = reacted.pop()
            else:
                reacted.append(a)
        except IndexError:
            reacted.append(a)
    print(len(reacted))

def part_2(polymer):
    reacted = collections.defaultdict(list)
    for a in polymer:
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if a.lower() == letter:
                continue
            try:
                if abs(ord(a) - ord(reacted[letter][-1])) == 32:
                    b = reacted[letter].pop()
                else:
                    reacted[letter].append(a)
            except IndexError:
                reacted[letter].append(a)
    print(sorted([len(v) for v in reacted.values()])[0])

if __name__ == '__main__':
    with open('input', 'r') as f:
        polymer = f.read().strip()
    part_1(polymer)
    part_2(polymer)
