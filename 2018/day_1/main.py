#!/usr/bin/env python3

import itertools

def part_1(df):
    f_final = sum(df)
    print(f_final)

def part_2(df):
    f_seen = set([0])
    f = 0
    for i in itertools.cycle(df):
        f += i
        if f in f_seen:
            break
        f_seen.add(f)
    print(f)

if __name__ == '__main__':
    with open('input', 'r') as f:
        df = [int(i) for i in f]
    part_1(df)
    part_2(df)
