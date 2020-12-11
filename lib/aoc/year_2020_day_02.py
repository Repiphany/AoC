#!/usr/bin/env python3

from .input import get_input
from collections import Counter

def test(args):
    assert valid_password('1-3 a: abcde')
    assert not valid_password('1-3 b: cdefg')
    assert valid_password('2-9 c: ccccccccc')
    assert valid_password2('1-3 a: abcde')
    assert not valid_password2('1-3 b: cdefg')
    assert not valid_password2('2-9 c: ccccccccc')
    print('Tests passed')

def valid_password(line):
    policy, password = line.strip().split(': ')
    r, c = policy.split(' ')
    low, high = (int(i) for i in r.split('-'))
    chk = Counter(password)
    return (low <= chk[c])*(chk[c] <= high)

def valid_password2(line):
    policy, password = line.strip().split(': ')
    r, c = policy.split(' ')
    a, b = (int(i) for i in r.split('-'))
    return (password[a-1] == c)^(password[b-1] == c)

def main(args):
    valid = sum(valid_password(line) for line in get_input(args.YEAR, args.DAY))
    print(valid)
    valid = sum(valid_password2(line) for line in get_input(args.YEAR, args.DAY))
    print(valid)
