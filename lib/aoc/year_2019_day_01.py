#!/usr/bin/env python3

from .input import get_input

def fuel(mass):
    return max(mass // 3 - 2, 0)

def fuelr(mass):
    fr = [fuel(mass)]
    while fr[-1]:
        fr.append(fuel(fr[-1]))
    return sum(fr)

def test(args):
    assert fuel(12) == 2
    assert fuel(14) == 2
    assert fuel(1969) == 654
    assert fuel(100756) == 33583
    assert fuelr(14) == 2
    assert fuelr(1969) == 966
    assert fuelr(100756) == 50346
    print('Tests passed')

def main(args):
    fuel_sum = fuelr_sum = 0
    for line in get_input(args.YEAR, args.DAY):
        fuel_sum += fuel(int(line))
        fuelr_sum += fuelr(int(line))
    print(fuel_sum)
    print(fuelr_sum)

