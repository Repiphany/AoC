#!/usr/bin/env python3

import argparse

def validate(passphrase):
    ps = passphrase.split(' ')
    return len(ps) == len(set(ps))

def validate_anagram(passphrase):
    ps = [str(sorted(p)) for p in passphrase.split(' ')]
    return len(ps) == len(set(ps))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', nargs = '?', default = 'input')
    args = parser.parse_args()
    with open(args.FILE, 'r') as f:
        passphrases = [line.strip() for line in f]
    print(sum(validate(p) for p in passphrases))
    print(sum(validate_anagram(p) for p in passphrases))
