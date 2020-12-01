#!/usr/bin/env python3

from .input import get_input
from .intcode import Intcode

def test(args):
    ic = Intcode('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
    ic.run()
    ic = Intcode('1102,34915192,34915192,7,4,7,99,0')
    ic.run()
    ic = Intcode('104,1125899906842624,99')
    ic.run()
    print('Tests passed')

def main(args):
    ic = Intcode(next(get_input(args.YEAR, args.DAY)), 1)
    ic.run()
    ic.initialize(2)
    ic.run()


