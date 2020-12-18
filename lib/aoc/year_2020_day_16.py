#!/usr/bin/env python3

from .input import get_input_chunks
from collections import Counter, defaultdict
from functools import lru_cache
import itertools
from IPython.terminal.embed import InteractiveShellEmbed

class Structure:
    def __init__(self, lines):
        info, your_ticket, nearby_tickets = lines
        self.data = {}
        for line in info.split('\n'):
            key, value = line.split(': ')
            r1, r2 = value.split(' or ')
            self.data[key] = (
                    [int(i) for i in r1.split('-')],
                    [int(i) for i in r2.split('-')],
                    )
        self.your_ticket = [int(i) for i in your_ticket.split('\n')[1].split(',')]
        self.nearby_tickets = []
        for line in nearby_tickets.split('\n')[1:]:
            if not line.strip():
                continue
            self.nearby_tickets.append([int(i) for i in line.split(',')])

        self.valid_tickets = [t for t in self.nearby_tickets if self.valid_ticket(t)] 

    @property
    def ranges(self):
        for pair in self.data.values():
            yield from pair

    def invalid_values(self, ticket):
        for value in ticket:
            if not any(a <= value <= b for a, b in self.ranges):
                yield value

    def valid_ticket(self, ticket):
        for value in ticket:
            if not any(a <= value <= b for a, b in self.ranges):
                return False
        return True

    def scanning_error_rate(self):
        return sum(v for ticket in self.nearby_tickets for v in
                self.invalid_values(ticket))

    def field_determination(self):
        self.fields = {i: set(self.data.keys()) for i in range(len(self.your_ticket))}
        def in_range(value, r):
            return r[0] <= value <= r[1]
        for ticket in self.valid_tickets:
            for i, v in enumerate(ticket):
                for field, (r1, r2) in self.data.items():
                    if not in_range(v, r1) and not in_range(v, r2):
                        self.fields[i].discard(field)
        while True:
            for i, v in self.fields.items():
                if len(v) == 1:
                    field, = v
                    for j, s in self.fields.items():
                        if i == j:
                            continue
                        s.discard(field)
            if all(len(v) == 1 for v in self.fields.values()):
                break
        for i, v in self.fields.items():
            field, = v
            self.fields[i] = field
        return self.fields

    def departure(self):
        fields = self.field_determination()
        m = 1
        for i, v in self.fields.items():
            if v.startswith('departure'):
                m *= self.your_ticket[i]
        return m

def test(args):
    shell = InteractiveShellEmbed()
    structure = Structure("""class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".split('\n\n'))
    shell()
    print('Tests passed')

def main(args):
    structure = Structure(get_input_chunks(args.YEAR, args.DAY, delimiter = '\n\n'))
    print(structure.scanning_error_rate())
    print(structure.departure())

