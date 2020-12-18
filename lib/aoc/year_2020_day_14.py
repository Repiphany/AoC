#!/usr/bin/env python3

from .input import get_input
from collections import Counter, defaultdict
from functools import lru_cache
import itertools
from IPython.terminal.embed import InteractiveShellEmbed
import re

class Bitmasker:
    def __init__(self, lines):
        self.mask = []
        for line in lines:
            if line.startswith('mask'):
                self.mask.append((line.split(' = ')[1], []))
            elif line.startswith('mem'):
                addr, value = (int(i) for i in re.findall('\d+', line))
                self.mask[-1][1].append((addr, value))
        self.addresses = {}

    def demask(self):
        for mask, memory in self.mask:
            ones = [q.start() for q in re.finditer('1', mask)]
            zeros = [q.start() for q in re.finditer('0', mask)]
            for addr, value in memory:
                value = list(f'{value:036b}')
                for one in ones:
                    value[one] = '1'
                for zero in zeros:
                    value[zero] = '0'
                self.addresses[addr] = int(''.join(value), 2)

    def decoder(self):
        for mask, memory in self.mask:
            ones = [q.start() for q in re.finditer('1', mask)]
            zeros = [q.start() for q in re.finditer('0', mask)]
            floating = [q.start() for q in re.finditer('X', mask)]
            for addr, to_write in memory:
                value = list(f'{addr:036b}')
                for one in ones:
                    value[one] = '1'
                for p in itertools.product(['0', '1'], repeat = len(floating)):
                    for i, v in zip(floating, p):
                        value[i] = v
                    n_addr = int(''.join(value), 2)
                    self.addresses[n_addr] = to_write

    def initialize(self):
        self.addresses = {}
        self.demask()
        return sum(self.addresses.values())

    def initialize_decode(self):
        self.addresses = {}
        self.decoder()
        return sum(self.addresses.values())


def test(args):
    shell = InteractiveShellEmbed()
    bitmasker = Bitmasker("""mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".split('\n'))
    assert bitmasker.initialize() == 165

    bitmasker = Bitmasker("""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n'))

    assert bitmasker.initialize_decode() == 208
    
    shell()
    print('Tests passed')

def main(args):
    bitmasker = Bitmasker(get_input(args.YEAR, args.DAY))
    print(bitmasker.initialize())
    print(bitmasker.initialize_decode())

