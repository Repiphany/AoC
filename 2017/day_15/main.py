#!/usr/bin/env python3

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        a = int(f.readline().split(' ')[-1])
        b = int(f.readline().split(' ')[-1])
    f_a = 16807
    f_b = 48271

    def gen(i, f):
        while True:
            i = (i*f)%2147483647
            yield i
    gen_a = gen(a, f_a)
    gen_b = gen(b, f_b)

    N = 40000000
    matches = 0
    for _ in range(N):
        a_bin = next(gen_a)
        b_bin = next(gen_b)
        matches += (a_bin%65536 == b_bin%65536)
    print(matches)

    def gen2(i, f, n):
        while True:
            i = (i*f)%2147483647
            if not i%n:
                yield i

    gen_a = gen2(a, f_a, 4)
    gen_b = gen2(b, f_b, 8)

    N = 5000000
    matches = 0
    for _ in range(N):
        a_bin = next(gen_a)
        b_bin = next(gen_b)
        matches += (a_bin%65536 == b_bin%65536)
    print(matches)
