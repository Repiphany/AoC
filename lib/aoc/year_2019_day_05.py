#!/usr/bin/env python3

from .input import get_input
from .intcode import Intcode

def test(args):
    print('Tests passed')

def main(args):
    ic = Intcode(next(get_input(args.YEAR, args.DAY)))
    ic.value = 1
    ic.run()
    ic.initialize()
    ic.value = 5
    ic.run()
    

