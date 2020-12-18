#!/usr/bin/env python3

from .input import get_input

class Timetable:
    def __init__(self, lines):
        lines = iter(lines)
        self.depart = int(next(lines))
        self.bus_ids = [(int(c), i) for i, c in enumerate(next(lines).split(',')) if c != 'x']

    def earliest(self):
        bus_id = min(self.bus_ids, key = lambda x: -self.depart%x[0])[0]
        wait_time = -self.depart % bus_id
        return wait_time * bus_id

    def sequential(self):
        def combined_offset(periodicity, bus, bus_offset, starting_offset):
            for i in range(bus):
                if (starting_offset + bus_offset + periodicity*i)%bus == 0:
                    return starting_offset + periodicity*i
        periodicity, offset = self.bus_ids[0]
        for bus, bus_offset in self.bus_ids[1:]:
            offset = combined_offset(periodicity, bus, bus_offset, offset)
            periodicity *= bus
        return offset

def test(args):
    timetable = Timetable("""939
7,13,x,x,59,x,31,19""".split('\n'))
    assert timetable.earliest() == 295
    assert timetable.sequential() == 1068781
    
    timetable = Timetable("""0
67,7,59,61""".split('\n'))
    assert timetable.sequential() == 754018
    print('Tests passed')

def main(args):
    timetable = Timetable(get_input(args.YEAR, args.DAY))
    print(timetable.earliest())
    print(timetable.sequential())

