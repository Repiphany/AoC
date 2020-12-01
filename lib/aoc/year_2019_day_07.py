#!/usr/bin/env python3

from .input import get_input
from .intcode import Intcode
import itertools

def test(args):
    assert feedback([9,8,7,6,5], '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5') == 139629729
    print('Tests passed')

def phase(setting, prog = None, initialize = True, amps = None, feedback = 0):
    if initialize:
        amps = [Intcode(prog) for _ in range(5)]
        for a, s in zip(amps, setting):
            a.initialize(s)
            a.return_output = True
    amps[0].value.append(feedback)
    for a, b in zip(amps, amps[1:]):
        signal = a.run()
        b.value.append(signal)
    return amps[-1].run()

def feedback(setting, prog):
    amps = [Intcode(prog) for _ in range(5)]
    for a, s in zip(amps, setting):
        a.initialize(s)
        a.return_output = True
    signal = phase(setting, amps = amps, initialize = False)
    while any(not a.halted for a in amps):
        new_signal = phase(setting, initialize = False, feedback = signal, amps = amps)
        if new_signal is not None:
            signal = new_signal
        else:
            break
    return signal

def main(args):
    prog = next(get_input(args.YEAR, args.DAY))
    print(max(phase(p, prog = prog) for p in itertools.permutations([0,1,2,3,4])))
    print(max(feedback(p, prog) for p in itertools.permutations([5,6,7,8,9])))

        


