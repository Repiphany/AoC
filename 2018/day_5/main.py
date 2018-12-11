#!/usr/bin/env python3

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

if __name__ == '__main__':
    with open('input', 'r') as f:
        polymer = f.read().strip()
    part_1(polymer)
