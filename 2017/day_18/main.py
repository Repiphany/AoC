#!/usr/bin/env python3

import argparse
import collections

class Program:
    def __init__(self):
        self.registers = collections.defaultdict(int)
        self.i = 0
        self.sounds = []

    def validate(self, x):
        try:
            x = int(x)
        except ValueError:
            x = self.registers[x]
        return x

    def snd(self, x):
        self.sounds.append(self.validate(x))

    def set(self, x, y):
        self.registers[x] = self.validate(y)

    def add(self, x, y):
        self.registers[x] += self.validate(y)

    def mul(self, x, y):
        self.registers[x] *= self.validate(y)

    def mod(self, x, y):
        self.registers[x] %= self.validate(y)

    def rcv(self, x):
        if self.validate(x) != 0:
            return self.sounds[-1]

    def jgz(self, x, y):
        if self.validate(x) > 0:
            return self.validate(y)
        return 1

    def run_instructions(self, instructions):
        while True:
            op, a = instructions[self.i]
            if op == 'jgz':
                self.i += self.jgz(*a)
            elif op == 'rcv':
                v = self.rcv(*a)
                if v:
                    return v
                self.i += 1
            else:
                getattr(self, op)(*a)
                self.i += 1

class Program2(Program):
    def __init__(self, n):
        self.registers = collections.defaultdict(int)
        self.registers['p'] = n
        self.queue = []
        self.target = None
        self.waiting = False
        self.i = 0
        self.sent = 0

    def snd(self, x):
        self.target.append(self.validate(x))
        self.sent += 1

    def rcv(self, x):
        try:
            self.registers[x] = self.queue.pop(0)
            self.waiting = False
        except IndexError:
            self.waiting = x
            return False
        return True

    def run_instructions(self, instructions):
        op, a = instructions[self.i]
        if self.waiting:
            if self.rcv(self.waiting):
                self.i += 1
                return
        if op == 'jgz':
            self.i += self.jgz(*a)
        elif op == 'rcv':
            if self.rcv(*a):
                self.i += 1
        else:
            getattr(self, op)(*a)
            self.i += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    instructions = []
    registers = collections.defaultdict(int)
    with open(args.FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            op, *a = line.split(' ')
            instructions.append((op, a))

    p = Program()
    print(p.run_instructions(instructions))

    p0, p1 = Program2(0), Program2(1)
    p0.target = p1.queue
    p1.target = p0.queue
    while True:
        p0.run_instructions(instructions)
        p1.run_instructions(instructions)
        if p0.waiting and p1.waiting:
            break
    print(p1.sent)

