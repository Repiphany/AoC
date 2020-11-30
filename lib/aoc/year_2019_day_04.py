#!/usr/bin/env python3

from .input import get_input

import itertools

def valid(password):
    return all[
            password > 99999,
            password < 1000000,
            len(list(itertools.groupby(str(password)))) < 6,
            str(password) == ''.join(sorted(str(password)))
            ]

def valid2(password):
    grouper = [(a, list(b)) for a, b in itertools.groupby(str(password))]
    return all[
            password > 99999,
            password < 1000000,
            len(grouper) < 6,
            any(len(b) == 2 for a, b in grouper),
            str(password) == ''.join(sorted(str(password))),
            ]

def test(args):
    assert valid(111111)
    assert not valid(223450)
    assert not valid(123789)
    assert valid2(112233)
    assert not valid2(123444)
    assert valid2(111122)
    print('Tests passed')

def main(args):
    pmin, pmax = [int(i) for i in next(get_input(args.YEAR, args.DAY)).split('-')]
    print(len([i for i in range(pmin, pmax) if valid(i)]))
    print(len([i for i in range(pmin, pmax) if valid2(i)]))

