#!/usr/bin/env python3

from .input import get_input
from .intcode import Intcode

def test(args):
    def ic_test(init, final):
        ic = Intcode(init)
        ic.run() 
        assert ic.state == final
    ic_test('1,9,10,3,2,3,11,0,99,30,40,50',
            '3500,9,10,70,2,3,11,0,99,30,40,50')
    ic_test('1,0,0,0,99', '2,0,0,0,99')
    ic_test('2,3,0,3,99', '2,3,0,6,99')
    ic_test('2,4,4,5,99,0', '2,4,4,5,99,9801')
    ic_test('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99')
    print('Tests passed')

def main(args):
    ic = Intcode(next(get_input(args.YEAR, args.DAY)))
    ic.prog[1] = 12
    ic.prog[2] = 2
    ic.run()
    print(ic.prog[0])
    p2 = 19690720
    for noun in range(100):
        for verb in range(100):
            ic.initialize()
            ic.prog[1] = noun
            ic.prog[2] = verb
            ic.run()
            if ic.prog[0] == p2:
                break
        else:
            continue
        break
    print(100*noun + verb)

