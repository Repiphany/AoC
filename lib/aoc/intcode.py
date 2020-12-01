#!/usr/bin/env python3

class Intcode:
    def __init__(self, prog):
        self.initial = prog
        self.prog = [int(i) for i in prog.split(',')]
        self.position = 0
        self.value = []
        self.debug = False
        self.return_output = False
        self.halted = False

    @property
    def state(self):
        return ','.join(str(i) for i in self.prog)

    def get(self, a, mode = 0):
        if mode == 0:
            return self.prog[a]
        elif mode == 1:
            return a

    def initialize(self, value = None):
        self.prog = [int(i) for i in self.initial.split(',')]
        self.position = 0
        self.halted = False
        self.value = []
        self.value.append(value)

    def add(self, modes = (0, 0, 0)):
        a, b, c = self.prog[self.position + 1: self.position + 4]
        mc, mb, ma = modes
        if self.debug:
            print('add', a, b, c, ma, mb, mc)
        self.prog[c] = self.get(a, ma) + self.get(b, mb)
        self.position += 4

    def multiply(self, modes = (0, 0, 0)):
        a, b, c = self.prog[self.position + 1: self.position + 4]
        mc, mb, ma = modes
        if self.debug:
            print('multiply', a, b, c, ma, mb, mc)
        self.prog[c] = self.get(a, ma) * self.get(b, mb)
        self.position += 4

    def save(self, modes = (0, 0, 0)):
        a = self.prog[self.position + 1]
        mc, mb, ma = modes
        try:
            self.prog[a] = self.value.pop(0)
        except AttributeError:
            self.prog[a] = self.value
        if self.debug:
            print('save', a, self.prog[a], modes)
        self.position += 2

    def output(self, modes = (0, 0, 0)):
        a = self.prog[self.position + 1]
        mc, mb, ma = modes
        if self.debug:
            print('output', a, modes)
        if self.return_output:
            self.position += 2
            return self.get(a, ma)
        else:
            print(self.get(a, ma))
        self.position += 2

    def jump_if_true(self, modes = (0,0,0)):
        a, b = self.prog[self.position + 1: self.position + 3]
        mc, mb, ma = modes
        if self.debug:
            print('jump_if_true', a, b, modes)
        if self.get(a, ma):
            self.position = self.get(b, mb)
        else:
            self.position += 3

    def jump_if_false(self, modes = (0,0,0)):
        a, b = self.prog[self.position + 1: self.position + 3]
        mc, mb, ma = modes
        if self.debug:
            print('jump_if_false', a, b, modes)
        if not self.get(a, ma):
            self.position = self.get(b, mb)
        else:
            self.position += 3

    def less_than(self, modes = (0,0,0)):
        a, b, c= self.prog[self.position + 1: self.position + 4]
        mc, mb, ma = modes
        if self.debug:
            print('less_than', a, b, c, modes)
        self.prog[c] = int(self.get(a, ma) < self.get(b, mb))
        self.position += 4

    def equals(self, modes = (0,0,0)):
        a, b, c= self.prog[self.position + 1: self.position + 4]
        mc, mb, ma = modes
        if self.debug:
            print('equals', a, b, c, modes)
        self.prog[c] = int(self.get(a, ma) == self.get(b, mb))
        self.position += 4

    def opcode(self):
        inst = self.prog[self.position]
        modes = (inst//10000, inst//1000%10, inst//100%10)
        op = {
                1:self.add,
                2:self.multiply,
                3:self.save,
                4:self.output,
                5:self.jump_if_true,
                6:self.jump_if_false,
                7:self.less_than,
                8:self.equals,
                99:None,
                }[inst%100]
        return op, modes

    def run(self):
        while not self.halted:
            op, modes = self.opcode()
            if op is None:
                self.halted = True
                return
            o = op(modes)
            if o is not None:
                return o

