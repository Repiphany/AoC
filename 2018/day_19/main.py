#!/usr/bin/env python3

import re
import collections
import itertools
import operator
import functools

primes = [2]

def is_prime(n, primes = primes):
    if n < 2:
        return False
    if n in primes:
        return True
    for p in primes:
        if p*p > n:
            return True
        if not n%p:
            return False
    while True:
        p = next_prime(p)
        primes.append(p)
        if p*p > n:
            return True
        if not n%p:
            return False

def next_prime(n):
    n += 1 + n%2
    while True:
        if is_prime(n):
            return n
        n += 2

def prime_factors(n):
    c = collections.Counter()
    p = 2
    while True:
        while not n%p:
            c.update([p])
            n //= p
        if n == 1:
            return c
        p = next_prime(p)

def divisors(n):
    pf, mul = zip(*prime_factors(n).items())
    for exps in itertools.product(*[range(n+1) for n in mul]):
        yield functools.reduce(operator.mul, (p**e for p, e in zip(pf, exps)), 1)

class Device:
    def __init__(self, registers, ip_register = 0):
        self.registers = registers
        self.ip_register = ip_register

    @property
    def ip(self):
        return self.registers[self.ip_register]

    @ip.setter
    def ip(self, value):
        self.registers[self.ip_register] = value

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

    def run_instruction(self, program):
        try:
            opcode, a, b, c = program[self.ip]
            getattr(self, opcode)(a, b, c)
            self.ip += 1
            return True
        except IndexError:
            return False

if __name__ == '__main__':
    program = []
    with open('input', 'r') as f:
        declaration = f.readline().strip()
        ip = int(declaration[-1])
        for i, line in enumerate(f):
            opcode = line.split(' ')[0]
            a, b, c = [int(i) for i in re.findall(r'\d+', line)]
            program.append((opcode, a, b, c))

    # part 1
    device = Device(registers = [0,0,0,0,0,0], ip_register = ip)
    r = set([0])
    # run program until it reaches first loop
    while True:
        device.run_instruction(program)
        if device.ip in r:
            break
        r.add(device.ip)
    print(sum(divisors(max(device.registers))))

    # part 2
    device = Device(registers = [1,0,0,0,0,0], ip_register = ip)
    r = set([0])
    # run program until it reaches first loop
    while True:
        device.run_instruction(program)
        if device.ip in r:
            break
        r.add(device.ip)
    print(sum(divisors(max(device.registers))))
