#!/usr/bin/env python3

import argparse

def captcha(s, n):
    return sum(int(a) for a, b in zip(s, s[n:] + s[:n]) if a == b)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        seq = f.read().strip()
    print(captcha(seq, 1))
    print(captcha(seq, len(seq)//2))
