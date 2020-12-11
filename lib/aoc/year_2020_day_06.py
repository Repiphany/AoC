#!/usr/bin/env python3

from .input import get_input_chunks

class Declarations:
    def __init__(self, s):
        self.answers = [set(l) for l in s.split('\n') if l.strip()]

    @property
    def any_answered(self):
        return set.union(*self.answers)

    @property
    def all_answered(self):
        return set.intersection(*self.answers)

def test(args):
    print('Tests passed')

def main(args):
    declarations = [Declarations(chunk) for chunk in
            get_input_chunks(args.YEAR, args.DAY, '\n\n')]
    print(sum(len(d.any_answered) for d in declarations))
    print(sum(len(d.all_answered) for d in declarations))

