#!/usr/bin/env python3

import itertools

def part_1(df):
    f_final = sum(df)
    print(f_final)

if __name__ == '__main__':
    with open('input', 'r') as f:
        df = [int(i) for i in f]
    part_1(df)
