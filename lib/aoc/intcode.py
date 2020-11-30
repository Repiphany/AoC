#!/usr/bin/env python3

class Intcode:
    def __init__(self, prog):
        self.initial = prog
        self.prog = [int(i) for i in prog.split(',')]
        self.position = 0

    @property
    def state(self):
        return ','.join(str(i) for i in self.prog)

    def initialize(self):
        self.prog = [int(i) for i in self.initial.split(',')]
        self.position = 0

    def add(self):
        a, b, c = self.prog[self.position + 1: self.position + 4]
        self.prog[c] = self.prog[a] + self.prog[b]
        self.position += 4

    def multiply(self):
        a, b, c = self.prog[self.position + 1: self.position + 4]
        self.prog[c] = self.prog[a] * self.prog[b]
        self.position += 4

    def run(self):
        while True:
            opcode = self.prog[self.position]
            if opcode == 99:
                return
            op = {
                    1:self.add,
                    2:self.multiply,
                    }[opcode]
            op()

