#!/usr/bin/env python3

from .input import get_input

import itertools

def test(args):
    print('Tests passed')

def main(args):
    expenses = set([int(l) for l in get_input(args.YEAR, args.DAY)])
    for e in expenses:
        if 2020 - e in expenses:
            print(e*(2020-e))
    for a, b, c in itertools.combinations(expenses, 3):
        if a+b+c == 2020:
            print(a*b*c)

