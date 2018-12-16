#!/usr/bin/env python3

import collections
import re
from IPython import embed

class Device:
    def __init__(self):
        self.registers = []
        self._opcodes = [ self.addr, self.addi, self.mulr, self.muli,
                self.banr, self.bani, self.borr, self.bori,
                self.setr, self.seti, self.gtir, self.gtri,
                self.gtrr, self.eqir, self.eqri, self.eqrr,
                ]
        self.opcodes = collections.defaultdict(list)

    def test(self, before, instruction, after):
        behavior = set()
        opcode, a, b, c = instruction
        for oper in self._opcodes:
            self.registers = before[:]
            oper(a, b, c)
            if self.registers == after:
                behavior.add(oper)
        self.opcodes[opcode].append(behavior)
        return len(behavior)

    def addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def setr(self, a, b, c):
        self.registers[c] = self.registers[a]

    def seti(self, a, b, c):
        self.registers[c] = a

    def gtir(self, a, b, c):
        self.registers[c] = 1 if (a > self.registers[b]) else 0

    def gtri(self, a, b, c):
        self.registers[c] = 1 if (self.registers[a] > b) else 0

    def gtrr(self, a, b, c):
        self.registers[c] = 1 if (self.registers[a] > self.registers[b]) else 0

    def eqir(self, a, b, c):
        self.registers[c] = 1 if (a == self.registers[b]) else 0

    def eqri(self, a, b, c):
        self.registers[c] = 1 if (self.registers[a] == b) else 0

    def eqrr(self, a, b, c):
        self.registers[c] = 1 if (self.registers[a] == self.registers[b]) else 0

if __name__ == '__main__':
    samples = []
    program = []
    with open('input', 'r') as f:
        for l in f:
            l = l.rstrip('\n')
            if not l:
                continue
            if l.startswith('Before'):
                before = [int(i) for i in re.findall('\d+', l)]
                instruction = [int(i) for i in re.findall('\d+', f.readline())]
                after = [int(i) for i in re.findall('\d+', f.readline())]
                samples.append((before, instruction, after))
                continue
            program.append([int(i) for i in re.findall('\d+', l)])

    device = Device()
    # part 1
    i = 0
    for sample in samples:
        if device.test(*sample) >= 3:
            i += 1
    print(i)

    # part 2
    opcodes = {}
    for k, v in device.opcodes.items():
        opcodes[k] = set.intersection(*v)
    identified = set()
    while True:
        for k in set(opcodes.keys()) - identified:
            if len(opcodes[k]) == 1:
                identified.add(k)
                opcodes[k], = opcodes[k]
                for v in opcodes.values():
                    if type(v) == set:
                        v.discard(opcodes[k])
        if len(opcodes.keys()) == len(identified):
            break

    device.registers = [0, 0, 0, 0]
    for line in program:
        opcode, a, b, c = line
        opcodes[opcode](a, b, c)
    print(device.registers[0])

