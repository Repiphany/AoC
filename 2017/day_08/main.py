#!/usr/bin/env python3

import argparse
import operator
import collections

oper_dict = { 'inc':operator.add, 'dec':operator.sub, '>':operator.gt,
        '<':operator.lt, '>=':operator.ge, '<=':operator.le,
        '==':operator.eq, '!=':operator.ne}

def closure(line, registers):
    r1, o1, n1, _, r2, o2, n2 = line.split(' ')
    o1, o2 = oper_dict[o1], oper_dict[o2]
    n1, n2 = int(n1), int(n2)
    def inst():
        registers[r1] = o1(registers[r1], n1)
    def cond():
        return o2(registers[r2], n2)
    return inst, cond

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    instructions = []
    registers = collections.defaultdict(int)
    with open(args.FILE, 'r') as f:
        for line in f:
            instructions.append(closure(line, registers))
    highest = 0
    for f, cond in instructions:
        if cond():
            f()
            highest = max(highest, max(registers.values()))
    print(max(registers.values()))
    print(highest)
