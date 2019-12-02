#!/usr/bin/env python3

import itertools

class Program:
    def __init__(self, fname):
        with open(fname, 'r') as f:
            self.intcode = tuple(int(i) for i in f.read().split(','))
        self.opcodes = {1:self.add, 2:self.multiply, 99:self.halt}

    def initialize(self):
        self.memory = list(self.intcode)
        self.pointer = 0

    def add(self):
        i, j, k = self.memory[self.pointer+1:self.pointer+4]
        self.memory[k] = self.memory[i] + self.memory[j]
        return True

    def multiply(self):
        i, j, k = self.memory[self.pointer+1:self.pointer+4]
        self.memory[k] = self.memory[i] * self.memory[j]
        return True
    
    def halt(self, args = 0):
        return False

    def run(self, a, b):
        self.initialize()
        self.memory[1] = a
        self.memory[2] = b
        while self.opcodes[self.memory[self.pointer]]():
            self.pointer += 4
        return self.memory[0]


if __name__ == '__main__':
    program = Program('input')
    # part 1
    print(program.run(12, 2))
    # part 2
    answer = 19690720
    for a, b in itertools.product(range(100), range(100)):
        if program.run(a, b) == answer:
            break
    print(100*a + b)


