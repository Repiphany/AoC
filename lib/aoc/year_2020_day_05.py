#!/usr/bin/env python3

from .input import get_input

def binary_partition(s):
    r, c = s[:7], s[-3:]
    table = str.maketrans('FLBR', '0011')
    row = int(str.translate(r, table), 2)
    column = int(str.translate(c, table), 2)
    seat_id = row*8 + column
    return row, column, seat_id

def find_gap(l):
    return next(a + 1 for a, b in zip(l, l[1:]) if b - a > 1)

def test(args):
    assert binary_partition('FBFBBFFRLR') == (44, 5, 357)
    print('Tests passed')

def main(args):
    seats = [binary_partition(l) for l in get_input(args.YEAR, args.DAY)]
    print(max(seats, key = lambda x : x[2])[2])
    ids = sorted(list(zip(*seats))[2])
    print(find_gap(ids))

