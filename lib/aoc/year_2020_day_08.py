#!/usr/bin/env python3

from .input import get_input
from IPython.terminal.embed import InteractiveShellEmbed

class Console:
    def __init__(self, lines):
        self.instructions = []
        for l in lines:
            op, i = l.split(' ')
            self.instructions.append((op, int(i)))
        self.position = 0
        self.accumulator = 0

    def acc(self, v):
        self.accumulator += v
        self.position += 1

    def jmp(self, v):
        self.position += v

    def nop(self, v):
        self.position += 1

    def exec_instruction(self):
        op, v = self.instructions[self.position]
        {
                'acc':self.acc,
                'jmp':self.jmp,
                'nop':self.nop,
                }[op](v)
    
    def run(self):
        seen = set([0])
        while True:
            try:
                self.exec_instruction()
                if self.position in seen:
                    return False
                seen.add(self.position)
            except IndexError:
                return True
    
    def fix_corruption(self):
        for i, inst in enumerate(self.instructions):
            self.position = 0
            self.accumulator = 0
            op, v = inst
            if op == 'nop':
                self.instructions[i] = ('jmp', v)
            elif op == 'jmp':
                self.instructions[i] = ('nop', v)
            else:
                continue
            if self.run():
                print(f'Instruction {i} changed from {op}')
                return self.accumulator
            else:
                self.instructions[i] = (op, v)

def test(args):
    console = Console("""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split('\n'))
    console.run()
    assert console.accumulator == 5
    assert console.fix_corruption() == 8
    print('Tests passed')

def main(args):
    console = Console(get_input(args.YEAR, args.DAY))
    console.run()
    print(console.accumulator)
    print(console.fix_corruption())

